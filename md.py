from mdutils.mdutils import MdUtils

mdFile = MdUtils(file_name='Example_Markdown',title='Date: 07-05-2021')


mdFile.new_header(level=2, title='sharmā ga.e lajā ga.e dāman chhuḌā ga.e', style='atx')


mdFile.new_header(level=3, title='Text', style='atx')
mdFile.new_line(mdFile.new_inline_link(link='https://rekhta.org/ghazals/sharmaa-gae-lajaa-gae-daaman-chhudaa-gae-jigar-moradabadi-ghazals', text='Rekhta'))
mdFile.write('  \n')
mdFile.new_header(level=3, title='Renditions & Recitations', style='atx')
mdFile.create_md_file()