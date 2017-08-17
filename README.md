# Sort-log-data-to-calculate-MTF
Find *.txt data from folders and dig out the useful MTF data from txt files

<h>How it works:</h>
    <div>Step1 - The script will find all necessary *.txt log files which contain camera MTF value at different ROI</div>
    <div>Step2 - Find the MTF data located in the log file with some key words</div>
    <div>Step3 - Output the MTF data with specified format and save in specified *.csv file</div>

Note:Tkinter window is used for simple GUI operation

In the py script, we make 3 main fucntions to do this work:

   <code>walk_Directory</code>
   This function will create a file name list with desired suffix name
   <code>data_read</code>
   Find the camera MTF test data with desired key word. After that, creat a list contain sample ID and MTF value with ROIs
   <code>data_save</code>
   Output the data(list) and save them into *.csv file

Simple and Easy

