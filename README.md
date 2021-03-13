<h1 align="center">AWS Developer Associate Certification</h1>

<div align="center">
    <img src="https://github.com/Shwetabh1/AWS_Certification/blob/master/Images/aws_cert.png" alt="AWS Developer"/>
</div>

## Foreword
Focus on the learning and certification will follow. Certification should never be the Target. Your ability to comprehend and apply those learnings should be.

## What is this?
> You can never understand everything but you should push yourself to understand the system.<br/>
> *-Ryan Dahl (creator of Node.JS)*

This a complete guide for achieving AWS certified developer mettle. It comprises of notes, lab works, exam break down, essential tips and probable questions could be asked. Each topic in the content has 3 sections; Notes, then the practical work you should do and lastly dozens of questions that can be asked in the AWS Certified Developer Exam related to that topic.

<b>NOTE: As per the NDA I have not disclosed any questions but steered people in the right direction.</b>

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

<b>IAM & Cognito</b><br>
<i>Questions will definetly be asked from IAM including IAM role for DynamoDB, Web Federation, Corporate network, CloudFront, Elastic Beanstalk, Cloud Formation and Elastic Cache. Cognito data sync, unauthenticated identities etc.</i>

<b>S3 ~ 10 Questions.</b><br>
<i>CORS, Static Hosting, S3 Encryption Header, S3 Performance optimisation(Mostly on adding uniqueness before the key), Bucket policy and ACL (basically how to restrict), Limits (like total bucket). Go through the FAQs.</i>

<b>DynamoDB ~ 12 Questions</b></br>
<i>Basic questions about Hash and range key, DynamoDBStreams, Throughput error (like if not Table then what is the cause), One question on write throughput calculation.  Go through the FAQs.</i>

<b>VPC</b></br>
<i>Scenario based questions revolving around assigning Elastic address or public address to access the instance and NAT in subnet, vpc flow logs etc</i>

<b>Kinesis</b></br>
<i>Questions related to Kinesis Client Library and resharding, etc.</i>

<b>AWS X-Ray</b></br> 
<i>Question related to tracing, embedding it with docker etc.</i>

<b>API Gateway</b></br> 
<i>Question related to stage variabled, invoking Lambda, deployments etc.</i>

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
1. Learn about Fargate and ECS. Also, when will you choose one over another?
1. Resharding (KCL), Evicting API cache (Default not DLB), Fargate, Glue and VPC/Security Groups.
1. Access Control Lists vs Security Group.
1. Questions from SAM and terraforms will certainly be asked.
1. Learn about Systems Manager Parameter Store.  

## Some Essential Tips
1. Practice Test is a must. I found tests from WHIZLABS quite helpful.
1. Lookout for scenario based questions.
1. Confirm big focus on DynamoDB (~15/55 questions) and S3 (~12/55 questions)
1. Attempt all questions as there are no negative marks.
1. If you have a long question, read the full question once and then only re read the last one or two lines as the real question lies there.
1. Practise the art of elimination! Eliminate the options that you are sure are not correct.

## Important Links
1. https://acloudguru.com/ [Course, personally recommended]
1. https://www.udemy.com/course/aws-certified-developer-associate-dva-c01/ [Course]
1. https://www.whizlabs.com/aws-developer-associate/ [Mock Test]
1. https://www.udemy.com/aws-certified-developer-associate-practice-tests-dva-c01/ [Mock Test]
1. https://d1.awsstatic.com/training-and-certification/docs-dev-associate/AWS_Certified_Developer_Associate-Exam_Guide_EN_1.4.pdf [Official Exam Guide]
