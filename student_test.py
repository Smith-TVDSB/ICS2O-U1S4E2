import pytest
import student 



def test_DirectorKevin():
    try:
        input_values=['Kevin Smith', 'Director']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert output[2]=='Director Smith'
    except:
        input_values=['Kevin Smith', 'Director']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        student.input = mock_input
        student.print = lambda s,t : output.extend([s,t])

        student.main()

        assert output[2]+' '+output[3]=='Director Smith'

def test_LlamaJuice():
    try:
        input_values=['Apple Juice', 'Llama']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert output[2]=='Llama Juice'
    except:
        input_values=['Apple Juice', 'Llama']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        student.input = mock_input
        student.print = lambda s,t : output.extend([s,t])

        student.main()

        assert output[2]+' '+output[3]=='Llama Juice'
 
def test_DoctorStrange():
    try:
        input_values=['Steven Strange', 'Doctor']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert output[2]=='Doctor Strange'
    except:
        input_values=['Steven Strange', 'Doctor']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        student.input = mock_input
        student.print = lambda s,t : output.extend([s,t])

        student.main()

        assert output[2]+' '+output[3]=='Doctor Strange'
 
def test_CaptainKirk():
    try:
        input_values=['Jame Kirk', 'Captain']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert output[2]=='Captain Kirk'
    except:
        input_values=['Jame Kirk', 'Captain']
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        student.input = mock_input
        student.print = lambda s,t : output.extend([s,t])

        student.main()

        assert output[2]+' '+output[3]=='Captain Kirk'
