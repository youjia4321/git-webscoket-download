<template>
  <div>
    <br />
    <strong>WebSocket测试</strong>
    <br />
    <br />
    <Input
      type="text"
      style="width: 350px"
      icon="ios-folder"
      v-model="text"
      placeholder="Enter message..."
      @keyup.enter.native="send"
    />
    <br />
    <br />
    <Button type="primary" @click="send">发送消息</Button>
    <br />
    <p v-for="(item, index) in messages" :key="index">
      <strong v-html="item"></strong>
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      path: "ws://127.0.0.1:8080/websocket",
      socket: "",
      text: "",
      messages: []
    };
  },
  created() {
    this.init();
  },
  methods: {
    init() {
      if (typeof WebSocket === "undefined") {
        alert("您的浏览器不支持socket");
      } else {
        // 实例化socket
        this.socket = new WebSocket(this.path);
        // 监听socket连接
        this.socket.onopen = this.open;
        // 监听socket错误信息
        this.socket.onerror = this.error;
        // 监听socket消息
        this.socket.onmessage = this.getMessage;
      }
    },
    open() {
      /* eslint-disable */
      console.log("socket连接成功");
    },
    error() {
      this.init();
      console.log("连接错误");
    },
    getMessage(e) {
      // 前端数据接收
      this.messages.push("服务器返回文件：" + e.data);
      var url = "http://127.0.0.1:8000/download/" + e.data;
      window.open(url);
    },
    send() {
      const download_file = 'documents/'+this.text
      this.socket.send(download_file);
      this.messages.push("下载文件：" + this.text);
      this.text = "";
    },
    close() {
      console.log("socket已经关闭");
    }
  },
  destroyed() {
    // 销毁监听
    this.socket.onclose = this.close;
  }
};
</script>

<style>
</style>