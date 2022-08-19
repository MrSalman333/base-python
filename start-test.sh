#! /usr/bin/env sh
set -e

echo "****************************** START:CI ****************************** /"
pytest #.....................................................start Unit Test 
ExitCodeResult=$? #............... assigne pytest exitcode to ExitCodeResult
echo pytest ExitCode = $ExitCodeResult #.................print  ExitCodeResult
if [ $ExitCodeResult -eq 0 ]
then
  echo "ExitCodeResult -eq 0"
  gh auth status
  gh pr  create --base MrSalman333 --head AbdulwahabDev:base-python-Abdulwahab
  echo "ExitCodeResult -eq 0"
else
  echo " ExitCodeResult -eq 1"
fi
echo "****************************** END:CI ****************************** /"

# gh --base MrSalman333:base-python --head AbdulwahabDev:base-python-Abdulwahab


gh pr  create --base MrSalman333 --head AbdulwahabDev:base-python-Abdulwahab