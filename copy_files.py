﻿import os
import shutil

def copy_files():
	"""
		Emplacement réservé aux tests
		
		Test #0: Pas de fichiers
		>>> copy_files()
		Total files copied : 0 (160 originals files)
		
	"""
	
	files = [
		'84217639',
		'54836761',
		'85527106',
		'20698438',
		'74025586',
		'72039685',
		'85805626',
		'20475443',
		'47506063',
		'74119390',
		'76451314',
		'86264050',
		'70375231',
		'88081891',
		'82143691',
		'75906628',
		'12545173',
		'997931',
		'9347983',
		'44407459',
		'79929271',
		'1238240',
		'72947608',
		'68971477',
		'80984431',
		'70243174',
		'73741291',
		'3296390',
		'58565662',
		'84346258',
		'68646070',
		'52263376',
		'20391649',
		'6630334',
		'86641237',
		'65146681',
		'32629645',
		'31900153',
		'84058987',
		'5212864',
		'27133375',
		'74400952',
		'66537559',
		'44951404',
		'45754267',
		'2395977',
		'3122684',
		'86180770',
		'16229722',
		'76001869',
		'8127067',
		'75090052',
		'45860167',
		'81254956',
		'3291545',
		'51922936',
		'62906428',
		'58730014',
		'3439881',
		'57609193',
		'86463145',
		'83677336',
		'10541755',
		'18774589',
		'3338540',
		'64022725',
		'64417207',
		'20643211',
		'29304610',
		'12959458',
		'86418487',
		'85910206',
		'74987575',
		'58382266',
		'61041706',
		'12392440',
		'64485940',
		'78585622',
		'10008988',
		'76370377',
		'81139480',
		'58325020',
		'2503207',
		'21827158',
		'13798714',
		'65836321',
		'2435634',
		'3268839',
		'74884141',
		'76883035',
		'9778294',
		'26209717',
		'30508228',
		'79329163',
		'63998944',
		'61309630',
		'58838530',
		'61401994',
		'24409927',
		'2254418',
		'60866755',
		'73582231',
		'63571888',
		'32899411',
		'16548979',
		'54166177',
		'66587317',
		'69876187',
		'1921919',
		'77744509',
		'70641400',
		'13312249',
		'233921',
		'50844466',
		'21213541',
		'31326577',
		'72014707',
		'56408656',
		'2503207',
		'10518157',
		'21827158',
		'21827158',
		'2593337',
		'83933260',
		'85012192',
		'7390552',
		'22749364',
		'16999216',
		'45600874',
		'31878433',
		'77524843',
		'61649041',
		'83643307',
		'71105080',
		'2876061',
		'1658757',
		'546012',
		'30461989',
		'2751257',
		'47536699',
		'88416808',
		'66426958',
		'78948727',
		'73315909',
		'17162650',
		'422524',
		'66302017',
		'61775431',
		'83880979',
		'76676593',
		'60873163',
		'46595032',
		'61401994',
		'41937484',
		'50749108',
		'73536601',
		'9623992',
		'50568268',
		'74888809',
		'59286079',
	]

	extensions = ['jpg', 'eps']

	file_copied = 0

	for number in files:
		racine = u"shutterstock_%s" % (number)
		
		for ext in extensions:
			filename = u"%s.%s" % (racine, ext)
			
			if os.path.exists(filename) and os.path.isfile(filename):
				# Copier le fichier dans un sous repertoire
				shutil.copyfile(filename, u"evoly/%s" % filename)
				print u"File %s copied ..." % filename
				file_copied += 1
				continue

	print u"Total files copied : %s (%s originals files)" % (file_copied, len(files))

# Appel de fonction
copy_files()

if __name__ == "__main__":
    import doctest
    doctest.testmod()