#include <Python.h>
#include <iostream>
#include <fstream>
#include <string>
int
main(int argc, char *argv[])
{
  Py_SetProgramName(argv[0]);  /* optional but recommended */
  Py_Initialize();
  FILE *fd = fopen("qr.py", "r");
  PyRun_SimpleFileEx(fd, "qr.py", 1);
  Py_Finalize();
  


  std::string line;
  std::ifstream myfile ("currentuser.txt");
  if (myfile.is_open())
  {
    while ( std::getline (myfile,line) )
    {
      std::cout << "READ "<<line << '\n';
    }
    myfile.close();
  }

  else std::cout << "Unable to open file"; 

  return 0;
}

