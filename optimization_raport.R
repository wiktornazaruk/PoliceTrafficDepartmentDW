# Optimization DW

# Data warehouse name: TrafficDepartmentDW 

# Size of the database (data warehouse): 2832.00 MB

# Count of giving tickets fact table: 9 818 924

# Count of rating of service fact table: 5 456 328

# Testing environment:

# 
# Device 
# 
# Processor	Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz   1.80 GHz 
# 
# Installed RAM	8.00 GB (7.85 GB usable) 
# 
# System type	64-bit operating system, x64-based processor 
# 
#   
# 
# Operating System						 
# 
# Edition		Windows 11 Pro for Workstations 
# 
# Version	23H2 
# 
# OS build	22631.3447 
# 
# Experience	Windows Feature Experience Pack 1000.22688.1000.0 
# 
#  
# 
# SSMS 
# 
# SQL Server Management Studio 19.2.56.2 
# 
# SQL Server Management Objects (SMO)						16.200.48050.0+9bd30730a8cbcdac9d9788ba6605f3dda96e6b89 
# 
# Microsoft T-SQL Parser						17.0.23.0+0d40faadb307b5d5fe930d64f47d2285ed3d0831 
# 
# Microsoft Analysis Services Client Tools						16.0.20054.0 
# 
# Microsoft Data Access Components (MDAC)					10.0.22621.3447 
# 
#  
# 
# Visual Studio 
# 
# Microsoft Visual Studio Community 2022 
# 
# Version 17.3.6 
# 
# VisualStudio.17.Release/17.3.6+32929.385 
# 
# SQL Server Analysis Services   16.0.20709.0 
# 
# Microsoft SQL Server Analysis Services Designer  
# 
# Version 16.0.20709.0 
# 
# SQL Server Data Tools   17.0.62207.04100 
# 
# Microsoft SQL Server Data Tools 
# 
# SsmsVsIntegration   1.0 


# Brief description of the queries:
# 1. (general one) - What are the top 5 places where the highest fine amount (in USD) was collected in 2023? 
# 2. (one with aggregations on dates) - What is the amount of collected fees for each month in 2022?
# 3. (one for a particular dimension attribute) - Are policeman with history of brutal arrests performing worse service?

# MESUREMENTS in [ms] (cache were cleared before every mesurement)

# MOLAP
# Estimated size: 71.29 MB
msize = 71.29
# load cube processing times (command end) in ms
mcpt <- c(56860, 53420, 46592, 31630, 32984, 32523, 31548, 31528, 30207, 31056)

# load query execution times (query cube end) in ms
mq1 <- c(174, 206, 170, 195, 174, 196, 167, 164, 184, 168)
mq2 <- c(156, 166, 162, 165, 180, 161, 148, 165, 162, 159)
mq3 <- c(142, 179, 138, 152, 141, 158, 154, 134, 133, 139)

# ROLAP
# Estimated size: 9.04 MB
rsize = 9.04
# load cube processing times (command end) in ms
rcpt <- c(14724, 5100, 5366, 5174, 5156, 10446, 4993, 11108, 5133, 10842)

# load query execution times (query cube end) in ms
rq1 <- c(431, 435, 431, 445, 426, 1108, 915, 1113, 990, 809)
rq2 <- c(357, 391, 355, 352, 377, 692, 664, 673, 698, 614)
rq3 <- c(1134, 1129, 1174, 1144, 1494, 4606, 4394, 4333, 3407, 2986)

# MOLAP with aggregation (by district , year, month, had history of brutal arrests)
# Estimated size: 82.11 MB
masize = 82.11
# load cube processing times (command end) in ms
macpt <- c(70462, 65389, 50606, 49370, 51473, 52916, 48347, 66855, 64303, 53194)

# load query execution times (query cube end) in ms
maq1 <- c(36, 25, 26, 31, 25, 41, 29, 36, 26, 21)
maq2 <- c(5, 10, 7, 5, 7, 6, 5, 4, 4, 3)
maq3 <- c(30, 14, 37, 31, 12, 15, 21, 28, 15, 11)

# size comparison data frame
sizedf <- data.frame(
  Type = c("MOLAP", "ROLAP", "MOLAP WITH AGGREGATION"),
  Size = c(msize, rsize, masize)
)
sizedf
#                     Type  Size
# 1                  MOLAP 71.29
# 2                  ROLAP  9.04
# 3 MOLAP WITH AGGREGATION 82.11

# cube processing times data frame 
cptdf <- data.frame(
  Type = c("MOLAP", "ROLAP", "MOLAP WITH AGGREGATION"),
  Mean = c(mean(mcpt), mean(rcpt), mean(macpt)),
  Sd = c(sd(mcpt), sd(rcpt), sd(macpt))
)
cptdf
#                     Type    Mean        Sd
# 1                  MOLAP 37834.8 10302.240
# 2                  ROLAP  7804.2  3609.134
# 3 MOLAP WITH AGGREGATION 57291.5  8412.245

# 1 query execution times data frame
q1df <- data.frame(
  Type = c("MOLAP", "ROLAP", "MOLAP WITH AGGREGATION"),
  Mean = c(mean(mq1), mean(rq1), mean(maq1)),
  Sd = c(sd(mq1), sd(rq1), sd(maq1))
)
q1df
#                     Type  Mean         Sd
# 1                  MOLAP 179.8  14.581571
# 2                  ROLAP 710.3 304.270731
# 3 MOLAP WITH AGGREGATION  29.6   6.292853

# 2 query execution times data frame
q2df <- data.frame(
  Type = c("MOLAP", "ROLAP", "MOLAP WITH AGGREGATION"),
  Mean = c(mean(mq2), mean(rq2), mean(maq2)),
  Sd = c(sd(mq2), sd(rq2), sd(maq2))
)
q2df
#                     Type  Mean         Sd
# 1                  MOLAP 162.4   8.154072
# 2                  ROLAP 517.3 160.998309
# 3 MOLAP WITH AGGREGATION   5.6   2.011080

# 3 query execution times data frame
q3df <- data.frame(
  Type = c("MOLAP", "ROLAP", "MOLAP WITH AGGREGATION"),
  Mean = c(mean(mq3), mean(rq3), mean(maq3)),
  Sd = c(sd(mq3), sd(rq3), sd(maq3))
)
q3df
#                     Type   Mean          Sd
# 1                  MOLAP  147.0   14.102797
# 2                  ROLAP 2580.1 1517.735554
# 3 MOLAP WITH AGGREGATION   21.4    9.347608
