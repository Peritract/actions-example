pkill -f app.py || true
cd langdale_zoo_api;
nohup python3 -u app.py &