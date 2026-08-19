import sys
E = ('eval (function(){var a=__SHOT.state();var r=__SHOT.press();var b=__SHOT.state();'
     'return "gt"+a.gt.toFixed(2)+" off"+a.handOff.toFixed(2)+" safe"+a.safeNow+" "+'
     '(a.active?a.active.k:"-")+" -> "+r+" | e"+b.escaped+" c"+b.caught+" w"+b.waiting+" s"+b.sheepLeft;})()')
first = int(sys.argv[1]) if len(sys.argv) > 1 else 1370
n = int(sys.argv[2]) if len(sys.argv) > 2 else 25
gap = int(sys.argv[3]) if len(sys.argv) > 3 else 1080
out = sys.argv[4] if len(sys.argv) > 4 else 'acts1.txt'
acts = ['wait %d' % first, E]
for _ in range(n):
    acts += ['wait %d' % gap, E]
acts += ['eval __SHOT.state()']
open(out, 'w', encoding='utf-8').write('\n'.join(acts))
print(len(acts))
