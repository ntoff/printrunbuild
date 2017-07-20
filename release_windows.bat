@rem redit dll needs to be in the printrun dir for it to build (apparently)
@copy "C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\msvcp90.dll" .\
@echo  Removing previous builds, if any
@if exist dist rmdir /S /Q dist > buildlog.log
@if not exist printrun\gcoder_line.pyd (
	@echo Attempting to build the memory efficient gcode viewer.
	@python.exe setup.py build_ext --inplace >> buildlog.log
	)
@echo Building...	
@python.exe setup_win.py py2exe -v >> buildlog.log
@echo Copying images...
@xcopy images dist\images\ /Y /E >> buildlog.log
@echo Copying locales...
@xcopy locale dist\locale\ /Y /E >> buildlog.log
@if exist Slic3r (
	@echo Copying Slic3r...
	@xcopy Slic3r dist\Slic3r\ /Y /E >> buildlog.log
	)
@echo Copying msvcp90.dll and printrunconf.ini... >> buildlog.log	
@copy MSVCP90.DLL dist\ >> buildlog.log
@copy printrunconf.ini dist\ >> buildlog.log
@echo Cleaning up...
@if exist build rmdir /S /Q build >> buildlog.log
@rem TODO: Get todays date and insert it here to signify when printrun was built
@ren dist "Printrun_date"
@echo Details were logged to buildlog.log
@pause
