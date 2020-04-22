FROM django:onbuild

COPY ./ ./

RUN pip install -r requirements.txt

CMD ["/bin/bash"]