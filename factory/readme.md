Factory Pattern / Abstract Factory Pattern

Based on how I see it, the goal of this design pattern is to bring in loose coupling between the top level client & many-variations of doer. 

Each Doer instance is expected to perform a common subset of functions. The Doer is expected to bring their own equipments. Nothing is provided. You are hired as consutants. You come, you do the job, and then you exit. No one will ever know you ever existed. Your USP is you get shit done with no heavy back & forth communication.

For eg. if you need SAP auditing done, you lay out the set of functionality you need. Then you can hire EY, PWC, Deloittee, Accenture, ZS_Associates, etc.. to come and do the job. They bring their own staff, their own styles, manage the vacation of employees, medical benefits, etc.. and all you have to care about is getting your needs done as long as they support the functionality you expect to get done.

