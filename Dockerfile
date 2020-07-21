FROM ubuntu

RUN apt-get update -q

# install wget, java, and mini-httpd web server
WORKDIR  /tmp
RUN apt-get install -yq wget
RUN apt-get install -yq default-jre-headless
RUN apt-get install -yq mini-httpd

# install elasticsearch
RUN wget -nv https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.5.tar.gz && \
    tar zxf elasticsearch-1.3.5.tar.gz && \
    rm -f elasticsearch-1.3.5.tar.gz && \
    mv /tmp/elasticsearch-1.3.5 /elasticsearch

# install kibana
RUN wget -nv https://download.elasticsearch.org/kibana/kibana/kibana-3.1.2.tar.gz && \
    tar zxf kibana-3.1.2.tar.gz && \
    rm -f kibana-3.1.2.tar.gz && \
    mv /tmp/kibana-3.1.2 /kibana


EXPOSE 8000 9200

CMD /elasticsearch/bin/elasticsearch -Des.logger.level=OFF & mini-httpd -d /kibana -h `hostname` -r -D -p 8000

