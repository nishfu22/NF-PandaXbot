
FROM python:3.9.2-slim-buster
COPY resources/startup/panda.sh .
RUN chmod +x panda.sh && sh panda.sh
WORKDIR /root/ilhammansiz/
CMD ["bash", "resources/startup/startup.sh"]
