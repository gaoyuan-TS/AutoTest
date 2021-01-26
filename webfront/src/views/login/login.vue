<template>
  <div class = "bkimage">
       <vue-particles
        color="#dedede"
        :particleOpacity="0.7"
        :particlesNumber="60"
        shapeType="circle"
        :particleSize="4"
        linesColor="#dedede"
        :linesWidth="1"
        :lineLinked="true"
        :lineOpacity="0.4"
        :linesDistance="150"
        :moveSpeed="2"
        :hoverEffect="true"
        hoverMode="grab"
        :clickEffect="true"
        clickMode="push"
        class="bkimage"
      >
      </vue-particles>
    <div class="wrap" id="wrap">
        <div class="logGet">
            <!-- 头部提示信息 -->
            <div class="logD logDtip">
                <p class="p1">登录</p>
            </div>
            <!-- 输入框 -->
            <div class="lgD">
                <i class = 'iconfont icon-denglu '></i>
                <input type="text" placeholder="输入用户名" v-model="loginForm.username"/>
            </div>
            <div class="lgD">
                <i class = 'iconfont icon-mima54'></i>
                <input type="password" placeholder="输入用户密码" v-model="loginForm.password" />
            </div>
            <div class="logC">
                <a><button @click="login">登 录</button></a>
            </div>
        </div>
    </div>

    </div>
</template>

<script>
import { mapMutations } from 'vuex';
export default {
    data() {
        return  {
            loginForm:{
                username: '',
                password: ''
                }
                   
            };

    },
        
    methods:{
        ...mapMutations(['changeLogin']),
      login: function() {
            let _this = this;
            if (this.loginForm.username === '' ) {
                this.$message.error("用户名不能为空");
            }
            else if ( this.loginForm.password === '') {
                this.$message.error("密码不能为空");
            }

            else  {
                _this.$axios({
                    method: 'post',
                    url: '/users/login',
                    data: _this.loginForm
                }).then(res =>{
                    console.log(res.data);
                    if (res.data.code != '200') {
                        this.$message.error(res.data.data);
                        
                    }
                        
                    else if (res.data.code =='200') {
                        this.$message.success('登录成功')
                        // _this.userToken = 'Bearer' + res.data.data.body.token;
                        // //将用户token保存到vuex中
                        // _this.changLogin({Authorization: _this_userToken});
                        _this.$router.push('../home')
                        
                    }
                }).catch(error => {
                    this.$message.error('登录失败');
                })
            }
            }     
      },
    }


</script>

<style scoped>
    .bkimage{
        background-size:100%;
        background: url("../../assets/image/background.jpg") no-repeat;
        width: 100%;
        height: 100%;
        position: absolute;
        overflow: hidden;
        -moz-background-size:60% 80%;
        -webkit-background-size:60% 80%;
        -o-background-size:60% 80%; 
        -webkit-background-size:100% 100%;
         }
    #wrap {
        height: 600px;
        width: 100%;
        background-position: center center;
        position: relative;
        
    }

    #head {
        height: 120px;
        width: 100;
        background-color: #66CCCC;
        text-align: center;
        position: relative;
    }

    #wrap .logGet {
        height: 408px;
        width: 368px;
        position: absolute;
        background-color: #FFFFFF;
        top: 100px;
        right: 15%;
    }

    .logC a button {
        width: 100%;
        height: 45px;
        background-color: #ee7700;
        color: white;
        font-size: 18px;
        border:0px;
        outline: #f37b04
    }

    .logGet .logD.logDtip .p1 {
        display: inline-block;
        font-size: 28px;
        margin-top: 30px;
        width: 86%;
        color: darkorange;
    }

    #wrap .logGet .logD.logDtip {
        width: 86%;
        border-bottom: 1px solid #ee7700;
        margin-bottom: 60px;
        margin-top: 0px;
        margin-right: auto;
        margin-left: auto;
    }

    .logGet .lgD img {
        position: absolute;
        top: 12px;
        left: 8px;
    }
    .logGet .lgD i {
        position: absolute;
        margin: 4px;
        top: 11px;
        left: 8px;
    }

    .logGet .lgD input {
        width: 100%;
        height: 42px;
        text-indent: 2.5rem;
        color: rgb(22, 17, 17);
        border-style:solid;
        border-color: #03a9f4;
      	box-shadow: 0 0 5px #03a9f4;
        outline:none

    }

    #wrap .logGet .lgD {
        width: 86%;
        position: relative;
        margin-bottom: 30px;
        margin-top: 30px;
        margin-right: auto;
        margin-left: auto;
    }

    #wrap .logGet .logC {
        width: 86%;
        margin-top: 0px;
        margin-right: auto;
        margin-bottom: 0px;
        margin-left: auto;
        border:0px;
    }


    .title {
        font-family: "宋体";
        color: #FFFFFF;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        /* 使用css3的transform来实现 */
        font-size: 36px;
        height: 40px;
        width: 30%;
    }

    .copyright {
        font-family: "宋体";
        color: #FFFFFF;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        /* 使用css3的transform来实现 */
        height: 60px;
        width: 40%;
        text-align: center;
    }


</style>




