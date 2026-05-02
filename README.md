# python-collaboration-project.py
Agile Velocity & Sprint Analyser:
Sprint: It is a short time-box period or mini project which a project team try to finish a specific set of tasks from the project backlog(Remianing tasks).
This program automate analysis of Agile sprint data. It changes traditional project management from manual spreadsheet to a programmable pandas environment with focus on evaluating team performance, and resource allocation.
Key items which are considered in this analysis are :Sprint velocity,Backlog rate, and Resource distribution, and Completion percentage.
For Sprint_Velocity it aggregates total Story_points from CSV file for completed tasks.Story_points is a unit of measurment which shows the total effort is needed for completing tasks with considering its complexity, effort, risk/ Uncertainty. We use Fibonacci sequence 1,2,3,5,8, 13, 21.. for it.  For Backlog_rate it calculates remaining effort to determine project milestone.For resource distibution it calculates individual workload to prevent team burnout and identify bottlenecks. Completion percentage provide real time indicator for current sprints' progress.
This is a sprint project which uses data set saved in a Sprint_Test.csv file. It helps to calculate the backlog and estimate remaining works and tasks. At the same time it shows you which tasks are finished and it shows your progress. 

Agile Risks analysis :
This part of code calculate mean, standard deviationa and variance of the Story_points.It calculate outliers which exceeds the treshhold.
This formula is : M + Std.dev


