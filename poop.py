label_value = subprocess.call(['powershell',
                               '-ExecutionPolicy',
                               'Bypass',
                               '.\\get_label.ps1',
                               "'{0}'".format(song_path),
                               "'{0}'".format(label_name)],
                              shell=True)
return str(label_value)