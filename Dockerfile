

FROM openmcworkshop/openmc_workshop_dependencies:openmc

RUN pip install streamlit

RUN git clone material_xs_plotter

WORKDIR material_xs_plotter

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "index.py"]

