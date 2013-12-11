

角色&服务
	1.master
		- task data
		- slave data
	2.slave
		- task run
	3.manage client
		- 提交任务
		- 查询和统计
启动期：
	1.master启动
	2.slave启动
		向master注册(约定心跳)
空档期
	1.slave心跳
		定时向master提交心跳(同时可获取新的心跳配置)
执行期：	
	1.下发任务
		manage client{task}-->master{ack,taskId}
	2.查询任务
		manage client{taskId}-->master{ack,task result}
	3.执行任务
		master{task}-->slave{ack}
	4.提交任务结果
		slaver{task result}-->master{ack}



通信形式：
	1.短消息
	2.请求返回uuid

通信协议格式:
	1.请求
		type:string,操作类型
		task:dict,任务信息
	2.响应
		uuid:int,唯一标识/taskId
		code:int,请求结果
		message:string,出错信息
		data:dict,详细信息
	

    
    
master
    .addJob
            操作：(接收到一个addJob请求)添加到任务队里中，并标记Job状态为"未指派"
            失败：无处理
    .getJob 
            操作：(接收到一个slave getJob请求)从任务队列中取一个Job，并标记Job状态为"已指派"
            失败：无处理
    .submitJob
            操作：(接收到一个slave submitJob请求)记录Job的结果，并标记Job状态为"已完成"
            失败：无处理

    .sendHeartbeat   
            操作：(接收到一个slave sendHeartbeat请求)更新slave队列，对未提交slaveId的请求，会生成一个slaveId并返回
            失败：无处理
            
    .cmd
            操作：(接收到一个命令)处理
            失败：无处理

slave
    .getJob 
            操作：向master请求一个Job
            失败：无处理
    .doJob
            操作：执行一个Job
            失败：提交状态为失败
    .submitJob
            操作：向master提交一个Job的处理结果
            失败：无处理
            
    .sendHeartbeat
            操作：向master提交一个心跳包，有slaveId的，要同时提交
            失败：无处理
    
    