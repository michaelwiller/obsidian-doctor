cd $(dirname $0)
if [ "$1" == "-h" ]; then
  printf "\nRunning python obsidian-doctor.py %s\n\n" "$@"
fi
. venv/bin/activate
python obsidian-doctor.py "$@"
deactivate # We're exiting anyway, and not expecting to be 'sourced' ... But just in case
