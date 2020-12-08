# -------------
# CS 143B - FALL 2020 - UNIVERSITY OF CALIFORNIA, IRVINE
# PROJECT 2
# NAME : VAANYA GUPTA
# STUDENT_ID : 92052177
# NET_ID : vaanyag
# -------------

def read_file(init,input):
    # -------------
    # Read the input files and calls the functions
    # that initializes the PM and translates the virtual
    # address to physical address.
    # -------------
    f1_init = open(init,"r")
    f1_input = open(input,"r") 

    lines = f1_init.readlines()
    in1 = lines[0].strip().split()
    in2 = lines[1].strip().split()
    V_A =  f1_input.readlines()
    virtual_adresses = V_A[0].strip().split()

    initialize(in1)
    initialize2(in2)
    calculate(virtual_adresses)
    f1_init.close()
    f1_input.close()

def initialize(in1):
    # -------------
    # Initializes the PM for line 1 in init text file.
    # -------------
    global PM,disk_resident,frames
    for init in range (0,len(in1),3):
        # Changes the state of the frame
        if int(in1[init+2])>0:
            frames[int(in1[init+2])] = -1
        # Initializes PM
        PM [2*int(in1[init])] = int(in1[init+1])
        PM [2*int(in1[init])+1] = int(in1[init+2])
        
def initialize2(in2):
    # -------------
    # Initializes the PM for line 2 in init text file.
    # -------------
    global PM,Disk
    for init in range (0,len(in2),3):
        if PM[2 * int(in2[init]) + 1] <= 0:
            Disk[abs(PM[2*int(in2[init])+1])][int(in2[init+1])] =  int(in2[init+2])
        else:
            PM[PM [2*int(in2[init])+1]*512 + int(in2[init+1])] = int(in2[init+2])
        if int(in2[init+2])>0:
            # Changes the state of the frame
            frames[int(in2[init+2])] = -1

def calculate(VA_init):
    # -------------
    # Derives s,p,w,pw and translates the virtual address to 
    # physical address
    # -------------
    global frames, PM

    for V_A in VA_init:
        bool,PA = True,-1
        V_A = int(V_A)
        VA = bin(V_A).replace("0b", "")
        extra =  (27-len (VA))
        VA = '0'*extra + VA
        s,p,w,pw = int((VA[0:-18]),2),int((VA[9:18]),2),int((VA[18::]),2),int((VA[9::]),2)
        
        # VA is outside of the segment boundary
        if pw>=PM[2*s]:
            bool = False

        # Page fault: PT is not resident 
        if PM[(2*s)+1]<0:
            for i in range(len(frames)):
                if frames[i] == 0:
                    frames[i]=-1
                    frame = i 
                    break

            b = abs(PM[2*s + 1])
            start = frame * 512
            for i in range(0,511):
                PM[start + i] = Disk[b][i]

            # Updates ST entry
            PM[2*s + 1] = frame 

        # Page fault: page is not resident        
        if PM[(PM[(2*s)+ 1]*512) + p] < 0:
            for i in range(len(frames)):
                if frames[i] == 0:
                    frames[i]=-1
                    frame = i 
                    break

            b = abs(PM[PM[2*s + 1]*512 + p])
            start = frame * 512
            for i in range(0,511):
                PM[start + i] = Disk[b][i]

            # Updates PT entry
            PM[PM[2*s + 1]*512 + p]=frame
        
        # Calculates physical address
        PA = PM[PM[(2*s)+1]*512+p]*512+w

        if bool:
            f.write(str(PA)+' ')
            print ('Virtual Address:',V_A,'Physical Address:',PA)
        else:
            f.write('-1'+' ')
            print ('Virtual Address:',V_A,'Physical Address:',-1,'(*error*)')

if __name__ == '__main__':

    PM, Disk = [0]*524288,[]

    # Initializing the Disk
    for i in range(512):
        Outer = []
        for j in range(1024):
            Outer.append(0)
        Disk.append(Outer)

    frames = [0]*512
    frames[0], frames[1]= -1,-1

    # Reading the input files and calculating the physical address
    f = open("output-no-dp.txt","w")
    read_file("init-no-dp.txt","input-no-dp.txt")
    f.close()
    f = open("output-dp.txt","w")
    read_file("init-dp.txt","input-dp.txt")
    f.close()