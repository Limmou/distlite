

��ɫ&����
	1.master
		- task data
		- slave data
	2.slave
		- task run
	3.manage client
		- �ύ����
		- ��ѯ��ͳ��
�����ڣ�
	1.master����
	2.slave����
		��masterע��(Լ������)
�յ���
	1.slave����
		��ʱ��master�ύ����(ͬʱ�ɻ�ȡ�µ���������)
ִ���ڣ�	
	1.�·�����
		manage client{task}-->master{ack,taskId}
	2.��ѯ����
		manage client{taskId}-->master{ack,task result}
	3.ִ������
		master{task}-->slave{ack}
	4.�ύ������
		slaver{task result}-->master{ack}



ͨ����ʽ��
	1.����Ϣ
	2.���󷵻�uuid

ͨ��Э���ʽ:
	1.����
		type:string,��������
		task:dict,������Ϣ
	2.��Ӧ
		uuid:int,Ψһ��ʶ/taskId
		code:int,������
		message:string,������Ϣ
		data:dict,��ϸ��Ϣ
	

    
    
master
    .addJob
            ������(���յ�һ��addJob����)��ӵ���������У������Job״̬Ϊ"δָ��"
            ʧ�ܣ��޴���
    .getJob 
            ������(���յ�һ��slave getJob����)�����������ȡһ��Job�������Job״̬Ϊ"��ָ��"
            ʧ�ܣ��޴���
    .submitJob
            ������(���յ�һ��slave submitJob����)��¼Job�Ľ���������Job״̬Ϊ"�����"
            ʧ�ܣ��޴���

    .sendHeartbeat   
            ������(���յ�һ��slave sendHeartbeat����)����slave���У���δ�ύslaveId�����󣬻�����һ��slaveId������
            ʧ�ܣ��޴���
            
    .cmd
            ������(���յ�һ������)����
            ʧ�ܣ��޴���

slave
    .getJob 
            ��������master����һ��Job
            ʧ�ܣ��޴���
    .doJob
            ������ִ��һ��Job
            ʧ�ܣ��ύ״̬Ϊʧ��
    .submitJob
            ��������master�ύһ��Job�Ĵ�����
            ʧ�ܣ��޴���
            
    .sendHeartbeat
            ��������master�ύһ������������slaveId�ģ�Ҫͬʱ�ύ
            ʧ�ܣ��޴���
    
    