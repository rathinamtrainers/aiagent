# Running Webapp
---
```bash
python ./src/webapp/main.py
```

### Check the webapp running status
```shell
sudo netstat -alnp | grep 8000
```

### Webapp HTTP Interface
http://127.0.0.1:8888

### Webapp SWAGGER Interface
http://127.0.0.1:8888/docs

### Webapp CURL interface
```bash
curl -X 'POST' \
  'http://127.0.0.1:8888/get_prompt_response' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "How is the weather",
  "model": "gemini-1.5-pro-001",
  "vdb": "Pinecone"
}'
```


# Running streamlit'
---
```shell
streamlit run ./src/ui/streamlit_app.py
```

### Check the streamlist app running status
```shell
sudo netstat -alnp | grep 8501
```

### Streamlist HTTP Interface
http://127.0.0.1:8501
