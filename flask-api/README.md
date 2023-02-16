### Example of flask api in docker container 

How to run:
1. Open docker 
2. Open anaconda prompt in project folder
3. Run command: docker build -t cont .
4. Run command: docker run -p 443:443 --name cont --rm cont
5. Send request to http://127.0.0.1:443/api/getScore