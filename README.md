# PROJECT 2 : VIRTUAL MEMORY

### **<ins>ABOUT</ins>**
A virtual memory program written in python language. It is a virtual memory(VM) system that uses segmentation and paging. It manages segment and page tables and translates virtual address to physical address. It supports demand paging. 

### **<ins>HOW TO RUN THE PROGRAM</ins>**
There are four input files: init-no-dp.txt, input-no-dp.txt, init-dp.txt and input-dp.txt file from where the program reads the commands line by line and prints the output to output-no-dp.txt for no dp input files and to ouput-dp.txt for dp input files. </br>
- The four input files, project2.py should be in the same directory. </br>
- To run the program: </br>
    - Make sure that the current directory is the same as the directory of four input files and project2.py</br>
    - Enter the command **<ins>python project2.py</ins>** in the terminal [if the current python version is set to 3] otherwise use **<ins>python3 project2.py</ins>**</br>
    - After the command is entered, output-no-dp.txt and output-dp.txt file is generated automatically and saved in the same directory as the four input files and project2.py</br>
- The output-no-dp.txt and output-dp.txt files contains the output of the program.

### **<ins>FUNCTIONS</ins>**

**<ins>read_file()</ins>**
- Reads the input files and call the functions that initializes the PM and translates the virtual address to physical address.

**<ins>initialize(in1)</ins>**
- Initializes the PM for line 1 in init text file.

**<ins>initialize2(in2)</ins>**
- Initializes the PM for line 1 in init text file.

**<ins>calculate(VA_init):</ins>**
- Derives s,p,w,pw; translates the virtual address to physical address and writes the physical address to the ouput file.  

### **<ins>AUTHOR</ins>**
VAANYA GUPTA
