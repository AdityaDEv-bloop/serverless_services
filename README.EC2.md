<!-- Commands To Connect to the EC2 Instance -->
<!-- Connecting to EC2 via SSH -->
<!-- Make Sure Serverless-Service-Key-pair-Ec2.pem file is located in root Directory -->
<!-- Reference https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install-ubuntu.html -->

1. chmod 400 "Serverless-Service-Key-pair-Ec2.pem"

2. ssh -i "Serverless-Service-Key-pair-Ec2.pem" ubuntu@ec2-54-179-168-163.ap-southeast-1.compute.amazonaws.com

3. sudo apt update

4. sudo apt install ruby-full

5. sudo apt install wget

<!-- Replace the Region Accordingly -->
6. wget https://aws-codedeploy-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/latest/install

7. chmod +x ./install

8. sudo ./install auto

9. sudo ./install auto > /tmp/logfile

<!-- Should See Active codedeploy agent service running -->
10. sudo service codedeploy-agent status

<!-- Output

    codedeploy-agent.service - LSB: AWS CodeDeploy Host Agent
        Loaded: loaded (/etc/init.d/codedeploy-agent; generated)
        Active: active (running) since Sat 2025-04-12 17:43:13 UTC; 1min 10s ago
        Docs: man:systemd-sysv-generator(8)
        Process: 2084 ExecStart=/etc/init.d/codedeploy-agent start (code=exited, status=0/SUCCESS)
        Tasks: 3 (limit: 1129)
        Memory: 65.1M (peak: 65.2M)
            CPU: 862ms
        CGroup: /system.slice/codedeploy-agent.service
                ├─2090 "codedeploy-agent: master 2090"
                └─2093 "codedeploy-agent: InstanceAgent::Plugins::CodeDeployPlugin::CommandPoller of master 2090"

    Apr 12 17:43:13 ip-172-31-23-39 systemd[1]: Starting codedeploy-agent.service - LSB: AWS CodeDeploy Host Agent...
    Apr 12 17:43:13 ip-172-31-23-39 codedeploy-agent[2084]: Starting codedeploy-agent:
    Apr 12 17:43:13 ip-172-31-23-39 systemd[1]: Started codedeploy-agent.service - LSB: AWS CodeDeploy Host Agent.
 -->

 11. d-E9MJC01PB

 severless-services-deployment-group

 less /opt/codedeploy-agent/deployment-root/67918741-84b2-4b83-8670-c9c9b502561b/d-F7RCNGDPB/logs/scripts.log
 d-KM5EN4UCO


 ssh -i "Serverless-Service-Key-pair-Ec2.pem" ubuntu@ec2-52-221-199-60.ap-southeast-1.compute.amazonaws.com