def test_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mydir')

    # base_temp will be the parent dir of 'mydir'
    # you don't have to use getbasetemp()
    base_temp = tmpdir_factory.getbasetemp()
    print('Base: ', base_temp)

    a_file = a_dir.join('something.txt')
    a_file.write("Hello World")
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('subfile.txt')
    another_file.write("Welcome back")
    

    for file in a_dir.listdir():
        print(file, "\n")
    
    # print(len(a_sub_dir.listdir()))