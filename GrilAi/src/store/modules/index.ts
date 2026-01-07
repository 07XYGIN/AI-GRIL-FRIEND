import { defineStore } from "pinia";
import { ref } from "vue";

const useUserStore = defineStore(
    "user",
    () => {
        const code = ref<string>("");

        const setCode = (co: string) => {
            code.value = co;
        };
        const getCode = ()=>{
            return code.value
        }
        return {
            code,
            setCode,
            getCode
        };
    },
    {
        persist: true,
    }
);

export default useUserStore;
