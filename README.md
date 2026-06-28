# ec2-s3-loop

## This Python script manages and evaluates the provisioning performance of mock AWS infrastructure assets. It begins by defining an `aws_sheet` function that utilizes `zip()` and `enumerate()` to pair and print the names of servers and S3 buckets side-by-side in a numbered list. 

## After displaying the assets, the program prompts the user to input an average spin-up time for an EC2 instance, casting the input into an integer for evaluation. This numerical value is processed through an `if/elif` conditional block to output a performance rating based on a target threshold of 60 seconds. 

## Finally, the script updates each individual server dictionary with a new `"spin_time"` key-value pair and loops through the updated list to print each server alongside its recorded timing value.
