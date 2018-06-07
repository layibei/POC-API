// 定义（路由）组件。
// 可以从其他文件 import 进来



var recommend = {
	template:`
	<div>
		<img src="https://ws1.sinaimg.cn/large/93838f95ly1fggker20l4j21hc0xcwfi.jpg" alt="">
	</div>
	`
}
var society = {
	template:`
	<div>
		<img src="https://ws1.sinaimg.cn/large/93838f95ly1fggkerb681j21hc0xcwfg.jpg" alt="">
	</div>
	`
}
var recreation = {
	template:`
	<div>
    	<img src="https://ws1.sinaimg.cn/large/93838f95ly1fggker6tmaj21hc0xc75b.jpg" alt="">
	</div>
	`
}
var military = {
	template:`
	<div>
    	<img src="https://ws1.sinaimg.cn/large/93838f95ly1fggkeqpmw4j21hc0xcdh1.jpg" alt="">
	</div>
	`
}
var education = {
	template:`
	<div>
    	<img src="https://ws1.sinaimg.cn/large/93838f95ly1fggkeqjmjsj21hc0xct9n.jpg" alt="">
	</div>
	`
}
// 路由配置    每个路由应该映射一个组件。
// new VueRoute 创建 router 实例，然后传 `routes` 配置
var router = new VueRouter({
	routes: [
		{
			path:"/recommend",
			component:recommend
		},
		{
			path:"/society",
			component:society
		},
		{
			path:"/recreation",
			component:recreation
		},
		{
			path:"/military",
			component:military
		},
		{
			path:"/education",
			component:education
		},
// 路由重定向，保证打开页面的时候显示在设置的页面中（本demo设置的为推荐页/recommend）
		{
			path:"*",
			redirect: "/recommend"
		}
	]
})
// 4. 创建和挂载根实例。（挂载路由）
// 记得要通过 router 配置参数注入路由，
// 从而让整个应用都有路由功能
new Vue({
	el:"#app",
	router:router
})
