import altair as alt
import pandas as pd

data=pd.DataFrame({
    "Personality traits" : ["Openness", "Extroversion", "Agreeableness", "Conscientiousness", "Neuroticism"],
    "values" : [8,6,9,3,1],
    "desc"   : ["Creative, happy to tackle new challenges", "Enjoys meeting new people", "Cares about others", "Dislikes structure and schedules", "Deals well with stress"]
             })
alt.Chart(data).mark_rect().encode(
    y='Personality traits',
    x='values',
    color='Personality traits',
    tooltip='desc',
).interactive()

