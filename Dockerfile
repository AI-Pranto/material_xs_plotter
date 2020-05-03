
# build with the following command
# sudo docker build -t gcr.io/material_xs_plotter-cloud-run/api:latest .
# run with 
# docker run gcr.io/material_xs_plotter-cloud-run/api:latest

FROM openmcworkshop/openmc_workshop_dependencies:openmc_nndc

RUN pip3 install streamlit

RUN git clone https://github.com/Shimwell/material_xs_plotter.git

WORKDIR material_xs_plotter

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "index.py"]

