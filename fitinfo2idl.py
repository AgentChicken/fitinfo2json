from sedfitter import write_parameters, write_parameter_ranges
import argparse
import pidly

# Truncate array to deal with IDl's dumbness
def truncate (arr):
    return arr
    if len(arr) <= 249:
        return arr
    else:
        return arr[0:249]

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("fitinfo", help="fitinfo file from which to extract parameters",
                    type=str)
args = parser.parse_args()

# Write out all models with a delta chi^2-chi_best^2 per datapoint < 3
write_parameters(args.fitinfo, 'parameters.txt',
                 select_format=('F', 3.))

# Write out the min/max ranges corresponding to the above file
write_parameter_ranges(args.fitinfo, 'parameter_ranges.txt',
                       select_format=('F', 3.))

# Open parameters.txt and read every line into an array
with open('parameters.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

# Shave off the first three lines - they're documentation
content = content[3:]

# Mark where new source sections begin
source_name_rows = []
for i in range(0, content.__len__()):
    if content[i].startswith("S"):
        source_name_rows.append(i)
source_name_rows.append(content.__len__())

# Split the parameter file into an array of arrays containing sources and their fits
# Each element in the array is an array containing strings, each of which is a line
# The first line in each element in each array within the array is the source name
# and other metadata, the rest of the lines are the actual fit data
sources_and_fits = []
for i in range(0, source_name_rows.__len__() - 1):
    sources_and_fits.append(content[source_name_rows[i]:source_name_rows[i + 1]])

# creates a json file with all of the relevant info
for sf in sources_and_fits:
    idl = pidly.IDL()
    meta = sf[0].split()
    #if int(meta[2]) > 249:
    #    meta[2] = "249"
    idl('s = {name: \'' + meta[0] + '\', n_data: ' + meta[1] + ', n_fits: ' + meta[2] + '}')
    model = []
    chi2 = []
    av = []
    scale = []
    time = []
    massc = []
    rstar = []
    tstar = []
    mdot = []
    rmax = []
    theta = []
    rmine = []
    mdisk = []
    rmaxd = []
    rmind = []
    rmind_au = []
    rc = []
    rchole = []
    zmin = []
    a = []
    b = []
    alpha = []
    rhoconst = []
    rhoamb = []
    mdotdisk = []
    incl = []
    av_int = []
    tau60 = []
    ldot = []
    h100 = []

    for line in sf[1:]:
        line_tokens = line.split()
        model.append(line_tokens[1])
        chi2.append(line_tokens[2])
        av.append(line_tokens[3])
        scale.append(line_tokens[4])
        time.append(line_tokens[5])
        massc.append(line_tokens[6])
        rstar.append(line_tokens[7])
        tstar.append(line_tokens[8])
        mdot.append(line_tokens[9])
        rmax.append(line_tokens[10])
        theta.append(line_tokens[11])
        rmine.append(line_tokens[12])
        mdisk.append(line_tokens[13])
        rmaxd.append(line_tokens[14])
        rmind.append(line_tokens[15])
        rmind_au.append(line_tokens[16])
        rc.append(line_tokens[17])
        rchole.append(line_tokens[18])
        zmin.append(line_tokens[19])
        a.append(line_tokens[20])
        b.append(line_tokens[21])
        alpha.append(line_tokens[22])
        rhoconst.append(line_tokens[23])
        rhoamb.append(line_tokens[24])
        mdotdisk.append(line_tokens[25])
        incl.append(line_tokens[26])
        av_int.append(line_tokens[27])
        tau60.append(line_tokens[28])
        ldot.append(line_tokens[29])
        h100.append(line_tokens[30])

    idl('model = ' + truncate(model).__str__())
    idl('chi2 = ' + truncate(chi2).__str__())
    idl('av = ' + truncate(av).__str__())
    idl('scale = ' + truncate(scale).__str__())
    idl('time = ' + truncate(time).__str__())
    idl('massc = ' + truncate(massc).__str__())
    idl('rstar = ' + truncate(rstar).__str__())
    idl('tstar = ' + truncate(tstar).__str__())
    idl('mdot = ' + truncate(mdot).__str__())
    idl('rmax = ' + truncate(rmax).__str__())
    idl('theta = ' + truncate(theta).__str__())
    idl('rmine = ' + truncate(rmine).__str__())
    idl('mdisk = ' + truncate(mdisk).__str__())
    idl('rmaxd = ' + truncate(rmaxd).__str__())
    idl('rmind = ' + truncate(rmind).__str__())
    idl('rmind_au = ' + truncate(rmind_au).__str__())
    idl('rc = ' + truncate(rc).__str__())
    idl('rchole = ' + truncate(rchole).__str__())
    idl('zmin = ' + truncate(zmin).__str__())
    idl('a = ' + truncate(a).__str__())
    idl('b = ' + truncate(b).__str__())
    idl('alpha = ' + truncate(alpha).__str__())
    idl('rhoconst = ' + truncate(rhoconst).__str__())
    idl('rhoamb = ' + truncate(rhoamb).__str__())
    idl('mdotdisk = ' + truncate(mdotdisk).__str__())
    idl('incl = ' + truncate(incl).__str__())
    idl('av_int = ' + truncate(av_int).__str__())
    idl('tau60 = ' + truncate(tau60).__str__())
    idl('ldot = ' + truncate(ldot).__str__())
    idl('h100 = ' + truncate(h100).__str__())

    idl_string = "p = { $\n"
    idl_string += "model:" + 'model' + ", $\n"
    idl_string += "chi2:" + 'chi2' + ", $\n"
    idl_string += "av:" + 'av' + ", $\n"
    idl_string += "scale:" + 'scale' + ", $\n"
    idl_string += "time:" + 'time' + ", $\n"
    idl_string += "massc:" + 'massc' + ", $\n"
    idl_string += "rstar:" + 'rstar' + ", $\n"
    idl_string += "tstar:" + 'tstar' + ", $\n"
    idl_string += "mdot:" + 'mdot' + ", $\n"
    idl_string += "rmax:" + 'rmax' + ", $\n"
    idl_string += "theta:" + 'theta' + ", $\n"
    idl_string += "rmine:" + 'rmine' + ", $\n"
    idl_string += "mdisk:" + 'mdisk' + ", $\n"
    idl_string += "rmaxd:" + 'rmaxd' + ", $\n"
    idl_string += "rmind:" + 'rmind' + ", $\n"
    idl_string += "rmind_au:" + 'rmind_au' + ", $\n"
    idl_string += "rc:" + 'rc' + ", $\n"
    idl_string += "rchole:" + 'rchole' + ", $\n"
    idl_string += "zmin:" + 'zmin' + ", $\n"
    idl_string += "a:" + 'a' + ", $\n"
    idl_string += "b:" + 'b' + ", $\n"
    idl_string += "alpha:" + 'alpha' + ", $\n"
    idl_string += "rhoconst:" + 'rhoconst' + ", $\n"
    idl_string += "rhoamb:" + 'rhoamb' + ", $\n"
    idl_string += "mdotdisk:" + 'mdotdisk' + ", $\n"
    idl_string += "incl:" + 'incl' + ", $\n"
    idl_string += "av_int:" + 'av_int' + ", $\n"
    idl_string += "tau60:" + 'tau60' + ", $\n"
    idl_string += "ldot:" + 'ldot' + ", $\n"
    idl_string += "h100:" + 'h100' + " $\n}"
    idl(idl_string)
    filename = meta[0].split('.')[-1]
    idl('SAVE, p, s, /VERBOSE, FILENAME = \'' + filename + '.sav\'')
    idl.close()
