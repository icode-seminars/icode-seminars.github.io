# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 22:32:43 2022

@author: Guilherme Mazanti
"""

import json
import locale
from datetime import datetime as dt

def format_speaker(speaker):
  res = ''
  url = False
  if "url" in speaker and speaker["url"]:
    url = True
    res += '<a href="{}" target="_blank">'.format(speaker["url"])
  res += '<em>'
  res += speaker["name"] + " (" + speaker["affiliation"] + ")"
  res += '</em>'
  if url:
    res += '</a>'
  return res

def write_seminar(seminar, file, last_row = False):
  global abs_count
  if last_row:
    cl = ' class="sem_table_td_bottom"'
  else:
    cl = ''
  file.write('<td{} style="text-align:center; vertical-align:top; width:90px;">\n'.format(cl))
  file.write('  <!-- TIME -->\n')
  file.write('  {}&ndash;{}\n'.format(seminar["time"][0], seminar["time"][1]))
  file.write('</td>\n')
  file.write('<td{}>\n'.format(cl))
  file.write('  <!-- TITLE -->\n')
  if "file" in seminar and seminar["file"]:
    file_path = seminar["file"] if "://" in seminar["file"] else "slides/" + seminar["file"]
    file.write('  <a href="{}"><img src="assets/images/download.png" alt="Download slides" style="height:24px;border:0"></a>&nbsp;&nbsp;\n'.format(file_path))
  file.write('  <strong>{}</strong><br />\n'.format(seminar["title"]))
  file.write('  <!--SPEAKER-->\n')
  if isinstance(seminar["speaker"], list):
    f_speakers = [format_speaker(spk) for spk in seminar["speaker"]]
  else:
    f_speakers = [format_speaker(seminar["speaker"])]
  file.write("  " + ", ".join(f_speakers) + "\n")
  file.write("<br />\n")
  file.write("  <!-- ABSTRACT -->\n")
  abstract = seminar["abstract"].replace('"', '&quot;')
  if "bio" in seminar and seminar["bio"]:
    abstract += "<br /><br /><strong>Bio.</strong>&nbsp;" + seminar["bio"].replace('"', '&quot;')
  file.write('  <script>document.write(insertAbstractToggle("{}", {}))</script>'.format(abstract, abs_count))
  abs_count += 1
  file.write('</td>\n')


def write_table(seminar_list, file):
  file.write('<table class="sem_table">\n')
  for s in seminar_list:
    file.write('  <tr>\n')

    file.write('    <td rowspan="{}" style="text-align:center; width:170px;" class="sem_table_td_bottom">\n'.format(len(s["seminars"])))
    date = dt.strptime(s["date"], "%Y-%m-%d")
    file.write('      <!-- DATE -->\n')
    file.write('      <strong>{}</strong><br />\n'.format(date.strftime("%d %B %Y")))
    file.write('      <!-- PLACE -->\n')
    file.write('      {}\n'.format(s["place"]))
    file.write('    </td>\n')
    write_seminar(s["seminars"][0], file, len(s["seminars"]) == 1)
    file.write('  </tr>\n')
    if len(s["seminars"]) > 1:
      file.write('  <tr>\n')
      for i, sem in enumerate(s["seminars"][1:]):
        write_seminar(sem, file, i == (len(s["seminars"]) - 2))
      file.write('  </tr>\n')
  file.write('</table>\n')

locale.setlocale(locale.LC_ALL, "en_US.utf8")
abs_count = 0

with open("seminars.json", "r", encoding = "utf-8") as file:
  seminars = json.load(file)

today = dt.today().strftime("%Y-%m-%d")
for i, s in enumerate(seminars):
  if today >= s["date"]:
    break
next_seminars = seminars[:i]
past_seminars = seminars[i:]

with open("../index.html", "w", encoding = "utf-8") as file:
  with open("_index.html", "r", encoding = "utf-8") as f:
    for line in f:
      if "<!-- NEXT SEMINARS -->" in line:
        if next_seminars:
          write_table(next_seminars[::-1], file)
      elif "<!-- PREVIOUS SEMINARS -->" in line:
        write_table(past_seminars, file)
      else:
        file.write(line)
