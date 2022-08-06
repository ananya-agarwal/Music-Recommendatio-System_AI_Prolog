#Design a song suggestion expert system in prolog that will suggest songs based on your mood and personality. 

Prolog code:
create :-
check(Song),
write('A song recommendation for you is '),write(Song).
create :-write('Sorry! No song found in the database').
object(religious) :- is_true('Do you like religious songs').
object(gym) :- is_true('Do you go to gym').
object(anger) :- is_true('Are you angry right now').
object(party) :- is_true('Do you have a party mood').
object(wedding) :- is_true('Do you like attending weddings').
object(beats) :- is_true('Are you having a mood of listening hip hop beats').
object(romantic) :- is_true('Are you a romantic person').
object(friends) :- is_true('Are you a person you has many friends').
object(old_age) :- is_true('Are you an aged person and like old songs').
object(latest) :- is_true('Are you a person who wanna try new things').
object(hollywood) :- is_true('Do you have mood of listening to hollywood songs').
object(bollywood) :- is_true('Do you have mood of listening to bollywood songs').
object(patriotic) :- is_true('Are you a patriotic person').
object(stress) :- is_true('Are you stressed out').
object(enjoyment) :- is_true('Wanna hear something for enjoyment').
object(journey) :- is_true('Do you like travelling').
object(jolly) :- is_true('Are you in a jolly mood').
object(mystery) :- is_true('Do you like mystery genre songs').
object(sad) :- is_true('Are you having a sad mood').
object(motivate) :- is_true('Wanna hear something to get motivated').
object(region) :- is_true('Are you a person who likes songs of a particular region and language').
object(afraid) :- is_true('Are you in a terrified mood').
object(tunes) :- is_true('Are you in a mood of hearing tunes').
check(zinda) :-
object(gym),
object(beats),
object(latest),
object(bollywood),
object(motivate).
check(challa_main_lad_jaava) :-
object(gym),
object(beats),
object(bollywood),
object(patriotic),
object(motivated).
check(chinta_ta_ta_chita_chita) :-
object(party),
object(wedding),
object(latest),
object(bollywood),
object(enjoyment),
object(jolly).
check(main_hoon_saath_tere) :-
object(friends),
object(bollywood),
object(romantic),
object(enjoyment),
object(beats).
check(dil_chahta_hai) :-
object(friends),
object(journey),
object(bollywood).
check(namo_namo) :-
object(religious),
object(anger),
object(bollywood),
object(stress),
object(journey),
object(sad),
object(afraid).
check(badtameez_dil) :-
object(party),
object(wedding),
object(bollywood),
object(beats),
object(latest),
object(stress),
object(enjoyment),
object(jolly).
check(pirates_of_the_caribbean_theme_song) :-
object(gym),
object(party),
object(beats),
object(stress),
object(journey),
object(latest),
object(hollywood),
object(enjoyment),
object(mystery).
check(baapu_sehat_ke_liye_tu_toh_hanikarak_hai) :-
object(gym),
object(bollywood),
object(motivate),
object(region).
check(navrai_majhi) :-
object(wedding),
object(bollywood),
object(stress),
object(enjoyment),
object(journey),
object(jolly),
object(region).
is_true(Q) :-
format("~w?\n", [Q]),
read(yes).
