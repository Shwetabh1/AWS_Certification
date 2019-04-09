<h1 align="center">AWS Developer Associate Certification</h1>

<div align="center">
    <img src="https://github.com/Shwetabh1/AWS_Certification/blob/master/Images/aws_cert.png" alt="AWS Developer"/>
</div>

## Foreword
Focus on the learning and certification will follow. Certification should never be the Target. Your ability to comprehend and apply those learnings should be.

## What is this?
> You can never understand everything but you should push yourself to understand the system.<br/>
> *-Ryan Dahl (creator of Node.JS)*

This a complete guide for achieving AWS certified developer mettle. It comprises of notes, lab works, exam break down, essential tips and probable questions that have been asked or could be asked. Each topic in the content has 3 sections; Notes, then the practical work you should do and lastly dozens of questions that can be asked in the AWS Certified Developer Exam related to that topic.

## Exam Details
<ul>
<li>Exam Duration: 130 Minutes</li>
<li>Total Questions: 65 Questions</li>
<li>Maximum Score 1000</li>
<li>Passing is 720</li>
<li>Resuts are available immediately.</li>
<li>In case you were unsuccessful you can always retake the exam, 14 days after yor first attempt.</li>
<li>The certification is valid for 3 years.</li>
</ul>

## Question Category Breakdown
<div align="center">

| Category      | Weightage     |
| ------------- |:-------------:|
| Deployment    | 22% |
| Security      | 26%     |
| Development with AWS Services | 30%    |
| Security      | 10%      |
| Monitoring and Troubleshooting      | 12%    |
</div>

<b><i>Special attention on Elastic Beanstalk, S3 & DyanmoDB.</b></i></br>

<b>IAM & Cognito ~ 5-6 Questions.</b><br>
<i>Questions will definetly be asked from IAM including IAM role for DynamoDB, Web Federation, Corporate network, CloudFront, Elastic Beanstalk, Cloud Formation and Elastic Cache. Cognito data sync, unauthenticated identities etc.
Options on authenticating using LDAP together with IAM.</i>

<b>S3 ~ 10 Questions.</b><br>
<i>CORS, Static Hosting, S3 Encryption Header, S3 Performance optimisation(Mostly on adding uniqueness before the key), Bucket policy and ACL (basically how to restrict), Limits (like total bucket</i>

<b>DynamoDB ~ 12 Questions</b></br>
<i>Basic questions about Hash and range key, DynamoDBStreams, Throughput error (like if not Table then what is the cause), One question on write throughput calculation.</i>

<b>VPC ~ 5 Questions</b></br>
<i>All scenario based 2-3 lines revolving around assigning Elastic address or public address to access the instance and NAT in subnet. One question related to VPC flow logs.</i>

<b>Kinesis ~ 2-3 Questions</b></br>
<i>Questions about Kinesis Client Library and resharding.</i>

<b>AWS X-Ray ~ 2-3 Questions</b></br> 
<i>Question related to tracing, embedding it with docker etc.</i>

<b>API Gateway</b></br> 
<i>Question related to solving api gateway autodeployment with SAM. Also how the user(client) can evict API gateway cache.</i>

<b>Elastic Beanstalk</b></br> 
<i>Question related to resources it can create, deployments, template, .ebextensions etc.</i>

<b>CloudFormation</b></br> 
<i>Question related to template sections, deployments.</i>

<b>Code Deploy</b></br> 
<i>Question related to deployment strategy, difference in on-premise and EC2 deployments.</i>

Note: 
1. Less questions from EC2 as they are focusing more on serverless.
1. Know/review limits for S3, DynamoDB, EC2, SNS, and SQS. 
1. Understanding the service limits would help with at least 5 questions.
1. Also know which AWS services are key-based and which platforms Elastic Beanstalk supports and which resources it can create.
1. One question about chosing Fargate over ECS when you don't want to take care of everything yourself and you can leave it to AWS :)
1. Resharding (KCL), Evicting API cache (Default not DLB), Fargate, Glue and VPC/Security Groups (?)
1. Access Control Lists vs Security Group.
1. Rest Questions were on AWS SDK, Default region (us-east-1) and Elastic Beanstalk Platforms and Elastic Cache to avoid the session state problem.
1. 1 Question was from SAM related to required properties on their template.
1. Questions from Systems Manager Parameter Store.  

## Some Essential Tips
1. Practice Test is a must. I found tests from WHIZLABS quite helpful.
1. Lookout for scenario based questions.
1. Confirm big focus on DynamoDB (~15/55 questions) and S3 (~12/55 questions)
1. Attempt all questions as there are no negative marks.
1. If you have a long question, read the full question once and then only re read the last one or two lines as the real question lies there.
1. Practise the art of elimination! Eliminate the options that you are sure are not correct.

## Important Links

1. https://learn.acloud.guru/course/aws-certified-developer-associate-june-2018/ [Course]
1. https://linuxacademy.com/amazon-web-services/training/course/name/aws-certified-developer-associate-2018 [Course]
1. https://www.whizlabs.com/aws-developer-associate/ [Mock Test]
1. https://www.udemy.com/aws-certified-developer-associate-practice-tests-dva-c01/ [Mock Test]
1. https://acloud.guru/forums/aws-certified-developer-associate/discussion/-KBkBPMHpN2ITSH1oDTO/passedwith90%25-myexamtips
1. https://acloud.guru/forums/aws-certified-developer-associate/discussion/-KUdI5f2LNbi4wvK7v4I/howtopassawscertified_deve
