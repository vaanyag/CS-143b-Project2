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
**<ins>CREATE</ins>**
- **create_init()** : Initializes: PCB[16], RCB[4] and Ready List RL with priority levels. It also creates PCB[0] (with priority = 0) 
- **create(p)** : Creates a new process with priority 'p' 

**<ins>DESTROY</ins>**
- **destroy(j)** : Destroys the process j if it exists along with its children and grandchildren (if any) </br>
- **check_destroy(j)**[<ins>Helper function of destroy()</ins>] : It checks if j is current running process or is one of the decendents of current running process and then calls the destroy function </br>
- **print_destroy_count()**[<ins>Helper function of destroy()</ins>] : Outputs the total number of processes destroyed </br>
- **remove_parent()**[<ins>Helper function of destroy()</ins>] : Remove j from the children list of its parent process when destroy is called </br>
    
**<ins>REQUEST</ins>**
- **request(r,k)** : Request k units of r resource 

**<ins>RELEASE</ins>**
- **release(r,k)** : Releases k units of resource r 

**<ins>TIMEOUT</ins>**
- **timeout()** : Moves the current process to the end of the reading list and call the scheduler  

**<ins>SCHEDULER</ins>**
- **scheduler()** : To perform context switch and schedule according to the priority 

**<ins>MANAGE INPUT AND OUTPUT</ins>**
- **write_in_file()** : Writes the output in the output file 
- **menu()** : Calls the appropriate function according to the command in the input file  

### **<ins>AUTHOR</ins>**
VAANYA GUPTA
