import time

def probar_streamlit(st):
    col1, col2 = st.columns(2)
    with col1:
        st.write("Agregue aquí botones, paneles, y opciones tal como se describe en el readme")
        st.button("Pulsameee")
    with col2:
        if st.button('Te gusta esto?'):
            st.text("""Bien hecho!
                                                              ___
                                                           .~))>>
                                                          .~)>>
                                                        .~))))>>>
                                                      .~))>>             ___
                                                    .~))>>)))>>      .-~))>>  
                                                  .~)))))>>       .-~))>>)>
                                                .~)))>>))))>>  .-~)>>)>
                            )                 .~))>>))))>>  .-~)))))>>)>
                         ( )@@*)             //)>))))))  .-~))))>>)>
                       ).@(@@               //))>>))) .-~))>>)))))>>)>
                     (( @.@).              //))))) .-~)>>)))))>>)>
                   ))  )@@*.@@ )          //)>))) //))))))>>))))>>)>
                ((  ((@@@.@@             |/))))) //)))))>>)))>>)>
               )) @@*. )@@ )   (\_(\-\p  |))>)) //)))>>)))))))>>)>
             (( @@@(.@(@ .    _/`-`  ~|b |>))) //)>>)))))))>>)>
              )* @@@ )@*     (@) (@)  /\p|))) //))))))>>))))>>
            (( @. )@( @ .   _/       /  \p)) //))>>)))))>>>_._
             )@@ (@@*)@@.  (6,   6) / ^  \p)//))))))>>)))>>   ~~-.
          ( @jgs@@. @@@.*@_ ~^~^~, /\  ^  \p/)>>))))>>      _.     `,
           ((@@ @@@*.(@@ .   \^^^/' (  ^   \p)))>>        .'         `,
            ((@@).*@@ )@ )    `-'   ((   ^  ~)_          /             `,
              (@@. (@@ ).           (((   ^    `\        |               `.
                (*.@*              / ((((        \        \      .         `.
                                  /   (((((  \    \    _.-~\     Y,         ;
                                 /   / (((((( \    \.-~   _.`" _.-~`,       ;
                                /   /   `(((((()    )    (((((~      `,     ;
                              _/  _/      `''''/   /'                  ;     ;
                          _.-~_.-~           /  /'                _.-~   _.'
                        ((((~~              / /'              _.-~ __.--~
                                           ((((          __.-~ _.-~
                                                       .'   .~~
                                                       :    ,'
                                                       ~~~~~
            """)
            time.sleep(5)
            st.experimental_rerun()
        else:
            st.write('Mas vale que lo oprimas ')

def abrir_musica(st):
    hp = "https://www.youtube.com/watch?v=6Ejga4kJUts&list=RDMM&index=22&ab_channel=TheCranberriesVEVO"
    st.video(hp)
