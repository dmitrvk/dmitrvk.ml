FROM lucaslorentz/caddy-docker-proxy:2.7

LABEL "caddy_0"="www.dmitrvk.ml"
LABEL "caddy_0.redir"="https://dmitrvk.ml{uri}"

ENTRYPOINT ["/bin/caddy"]

CMD ["docker-proxy"]
