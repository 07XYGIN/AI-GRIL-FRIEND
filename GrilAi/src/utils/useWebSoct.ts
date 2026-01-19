import { ref, onMounted, onUnmounted } from 'vue';
function useWebSocket(url: string) {
  const ws = ref<WebSocket | null>(null);
  const messages = ref<string>('');
  const isConnected = ref<boolean>(false);
  const i = ref(0);
  const MAX_RETRY = 3;
  /**发送消息 */
  const sendMsg = (data: string) => {
    ws.value?.send(data);
  };

  /**掉线重连 */
  const reconnect = () => {
    if (!ws.value) return;
    if (i.value >= MAX_RETRY) {
      isConnected.value = false;
      return;
    }
    if (ws.value?.readyState === WebSocket.CLOSED) {
      console.log('尝试重新连接.....');
      setTimeout(() => {
        ws.value = new WebSocket(url);
        setupWebSocket();
        i.value += 1;
      }, 3000);
    }
  };

  /**状态代理 */
  const setupWebSocket = () => {
    if (!ws.value) return;
    /**连接成功 */
    ws.value.onopen = () => {
      console.log('连接成功');
      isConnected.value = true;
    };
    /**连接关闭 */
    ws.value.onclose = () => {
      console.log('连接已关闭');
      isConnected.value = false;
      reconnect();
    };
    /**连接错误 */
    ws.value.onerror = () => {
      isConnected.value = false;
    };
    /**消息 */
    ws.value.onmessage = (e: MessageEvent) => {
      messages.value = e.data;
      console.log(messages.value);
      console.log(e.data);
    };
  };
  /**心跳检测 */
  const heartbeat = () => {
    if (!isConnected.value) {
      ws.value?.close();
      return;
    }
    setInterval(() => {
      sendMsg('ping');
    }, 30000);
  };
  onMounted(() => {
    ws.value = new WebSocket(url);
    setupWebSocket();
    heartbeat();
  });
  onUnmounted(() => {
    ws.value?.close();
    isConnected.value = false;
  });
  return {
    ws,
    sendMsg,
    messages,
    isConnected,
  };
}

export default useWebSocket;
