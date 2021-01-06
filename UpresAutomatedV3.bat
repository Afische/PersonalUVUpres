:: Upres and Conversion Automated

ECHO OFF
ECHO/
title Upres Conversion Batch

set /p expressions="Enter all expressions to process separated by spaces or semicolons: "
break > dothese.txt
for %%f in (%expressions%) do echo %%f >> dothese.txt

ECHO/
ECHO ~~~~~~~~Creating dothese.txt~~~~~~~~
ECHO/
ECHO ~~~~~~~~Creating config.txt~~~~~~~~
ECHO/

SET subjectDir=%~dp0
ECHO %subjectDir:~0,-1% > config.txt

ECHO ~~~~~~~~Removing Whitespace From dothese.txt and config.txt~~~~~~~~
ECHO/
ECHO ~~~~~~~~Copying UVs~~~~~~~~
ECHO/

MD tempExps
C:\Python38\python.exe %subjectDir%UVStuff.py

ECHO ~~~~~~~~Copying ICT Cams and ColorChart~~~~~~~~
ECHO/

for /d %%A in (.\expressions\*) do (
	if EXIST %%~fA\*.txt (
		ECHO %%~fA\ already contains an ICTcam or ColorChart
		ECHO/
	) ELSE (
		xcopy .\ICT_cams_and_colorchart %%~fA
	ECHO Dood, ICTcams and ColorChart were saved in this directory:
	ECHO %%~fA
	ECHO/
	)
)

FOR /f %%i in (%subjectDir%dothese.txt) do (
	ECHO/
	ECHO ~~~~~~~~Running Upres~~~~~~~~
	ECHO/
	C:
	CD \PAVO2019\Software_pipeline\Scripts\AutoPipeline
	C:\Python38\python RunUpres.py %subjectDir:~0,-1% %%i %%i
	ECHO/
	ECHO ~~~~~~~~Running Conversion~~~~~~~~
	ECHO/
	%subjectDir:~0,2%
	CD %subjectDir:~0,-1%
	C:\bin\final_convert config.txt %subjectDir%tempExps\exp%%i.txt
)
RMDIR /S /Q %subjectDir%tempExps

ECHO/
ECHO ~~~~~~~~All Done, Dood~~~~~~~~
ECHO/

PAUSE

::SET /a x=0
::FOR /f %%i in (%subjectDir%tempSmall) do (
::	SET expSmall[x]=%%i
::)
::SET /a y=0
::FOR /f %%i in (%subjectDir%tempLarge) do (
::	SET expLarge[y]=%%i
::)
::C:\Python38\python RunUpres.py %subjectDir:~0,-1% %expSmall[x]% %expLarge[y]%