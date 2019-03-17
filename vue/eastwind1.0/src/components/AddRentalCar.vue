<template>
  <div id="addrentalcar">
 	<h2>添加租车数据</h2>
   <form >
     <hr>
     <label>车牌</label>
     <input type="text" v-model="user.carid" required />
     <br>
     <label>出发地点</label>
     <input type="text" v-model="user.srcaddr" required />
     <br>
     <label>到达地点</label>
     <input type="text" v-model="user.dstaddr" required />
     <button v-on:click.prevent="singledataGet">获取数据</button>
   </form>
   <hr>
   <div id="preview">
     <h2>车牌: {{user.carid}}</h2>
     <h2>出发地点: {{user.srcaddr}}</h2>
     <h2>到达地点: {{user.dstaddr}}</h2>
   </div>
  </div>
</template>

<script>
export default {
  name: 'addrentalcar',
  data () {
    return {
      user:{
          carid:"",
          srcaddr:"",
          dstaddr:""
      },
      token_id:""
    }
  },
  methods:{
    post:function(){
      this.$http.post("http://jsonplaceholder.typicode.com/posts",{
        title:this.blog.title,
        body:this.blog.content,
        userId:1
      })
        .then(function(data){
          console.log(data);
          this.submmited=true;
        });
    },
    singledataGet:function(){
      this.$axios({
                method:'get',
                url:'http://127.0.0.1:8000/eastcars/1/'
                //headers:{"Content-Type":"application/json"},
                //data:{"username":"zte", "password":"zte123456"}
    })
    .then(res =>{
      console.log("Get data success")
      console.log(res.data)
      this.user.carid = res.data["carid"]
      this.user.srcaddr = res.data["srcaddr"]
      this.user.dstaddr = res.data["dstaddr"]
    })
    .catch(error =>{
      console.log("Get data failed")
      console.log("error")
    })}
  },
  created:function(){
    // this.$http.post(
    //   "http://127.0.0.1:8000/api-token-auth/", 
    //   {"username":"zte", "password":"zte123456"},
    //   {headers:{"Content-Type":"application/json"}},
    //   {"Access-Control-Allow-Origin":"*"}).then(res => {
    //   console.log("111111111!!!!!")
    //   this.user.carid="su999"
    // }).catch(error => {
    //   console.log("222222222222")
    //   console.log("error")
    // })
    this.$axios({
                method:'post',
                url:'http://127.0.0.1:8000/api-token-auth/',
                //headers:{"Content-Type":"application/json"},
                data:{"username":"zte", "password":"zte123456"}
    }).then(res => {
      this.user.carid="su999"
      this.token_id = res.data["token"]
      console.log(this.token_id)
    }).catch(error => {
      console.log("error")
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#addrentalcar *{
  box-sizing: border-box;
}
label{
  display: block;
  margin: 20px 0 10px;
}
</style>
