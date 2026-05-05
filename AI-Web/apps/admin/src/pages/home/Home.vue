<template>
  <div class="home-page">
    <el-row :gutter="20">
      <el-col :xs="24" :sm="12" :lg="8">
        <el-card shadow="hover">
          <template #header>概览</template>
          <el-statistic title="在线用户" :value="128" />
        </el-card>
      </el-col>

      <el-col :xs="24" :sm="12" :lg="8">
        <el-card shadow="hover">
          <template #header>今日新增</template>
          <el-statistic title="新增内容" :value="32" />
        </el-card>
      </el-col>

      <el-col :xs="24" :sm="12" :lg="8">
        <el-card shadow="hover">
          <template #header>系统状态</template>
          <el-tag type="success" size="large">运行正常</el-tag>
        </el-card>
      </el-col>
    </el-row>

    <el-card class="content-card" shadow="never">
      <template #header>首页内容区</template>
      <el-empty description="这里是右侧主内容区域，可继续接入业务模块" />
    </el-card>
  </div>
</template>
<script setup lang="ts">
import {useUserStore} from "@/store/modules/user.ts";
import {onMounted} from "vue";
const userInfo = useUserStore();

onMounted(() => {
  userInfo.getUser();
});
</script>
<style scoped>
.home-page {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.content-card {
  min-height: 320px;
}
</style>
