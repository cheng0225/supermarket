<template>
    <el-table :data="logs_data" style="width: 100%" :row-class-name="tableRowClassName">
        <el-table-column prop="employee" label="员工" width="250">
        </el-table-column>
        <el-table-column prop="merchant" label="所属商家" width="">
        </el-table-column>
        <el-table-column prop="time" label="操作时间" width="">
        </el-table-column>
        <el-table-column prop="txt" label="备注">
        </el-table-column>
    </el-table>
</template>
  
<style>
.el-table .warning-row {
    background: rgb(215, 175, 180);
}

.el-table .success-row {
    background: #c5e4eb;
}
</style>
  
<script>
import { get_logs } from '@/api/home.js'
export default {
    data() {
        return {
            msg: '',
            logs_data: [],
        }
    },

    mounted () {
        this.show_logs();
    },

    methods: {
        tableRowClassName({ row, rowIndex }) {
            if (rowIndex % 2)
                return 'warning-row';
            return 'success-row';
        },
        show_logs() {
            get_logs().then(
                response => {
                    this.logs_data = response.data
                },
                error => {
                    this.msg = "连接服务器失败";
                    console.log(error);
                }
            )
        }
    },
}
</script>