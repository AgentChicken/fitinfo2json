pro json2idl

file = DIALOG_PICKFILE(FILTER='*.txt'
OPENR, lun, file, /GET_LUN

array = ''
line = ''
WHILE NOT EOF(lun) DO BEGIN & $
  READF, lun, line & $
  array = [array, line] & $
ENDWHILE

FREE_LUN, lun

final_string = ''
FOREACH element, array DO final_string = final_string + element

json_struct = JSON_PARSE(final_string, /TOSTRUCT)

desig_names = TAG_NAMES(json_struct)

lim = N_ELEMENTS(desig_names) - 1

FOR i=0,lim DO BEGIN
  s = {DESIG: (tag_names(json_struct))[i], n_data: json_struct.(i).n_data, n_fits: json_struct.(i).n_fits}
  p = {model: json_struct.(i).model, $
       chi2:  json_struct.(i).chi2, $
       av: json_struct.(i).av, $
       scale: json_struct.(i).scale, $
       time: json_struct.(i).time, $
       massc: json_struct.(i).massc, $
       rstar: json_struct.(i).rstar, $
       tstar: json_struct.(i).tstar, $
       mdot: json_struct.(i).mdot, $
       rmax: json_struct.(i).rmax, $
       theta: json_struct.(i).theta, $
       rmine: json_struct.(i).rmine, $
       mdisk: json_struct.(i).mdisk, $
       rmaxd: json_struct.(i).rmaxd, $
       rmind: json_struct.(i).rmind, $
       rmind_au: json_struct.(i).rmind_au, $
       rc: json_struct.(i).rc, $
       rchole: json_struct.(i).rchole, $
       zmin: json_struct.(i).zmin, $
       a: json_struct.(i).a, $
       b: json_struct.(i).b, $
       alpha: json_struct.(i).alpha, $
       rhoconst: json_struct.(i).rhoconst, $
       rhoamb: json_struct.(i).rhoamb, $
       mdotdisk: json_struct.(i).mdotdisk, $
       incl: json_struct.(i).incl, $
       av_int: json_struct.(i).av_int, $
       tau60: json_struct.(i).tau60, $
       ldot: json_struct.(i).ldot, $
       h100: json_struct.(i).h100 $
       }
  fn = (tag_names(json_struct))[i] + '.sav'
  SAVE, json_struct, p, s, FILENAME = fn
ENDFOR

end
