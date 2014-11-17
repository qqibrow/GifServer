from moviepy.editor import *
clip = (VideoFileClip("./uploads/20141115_155758.mp4", audio=False).subclip((0,00.05),(0,02.00)).resize(0.3))
text = (TextClip("Working hard to DEMO!", fontsize=30, color='white',font='Amiri-Bold').set_pos((0,0)).set_duration(clip.duration))
composition = CompositeVideoClip([clip, text])
composition.write_gif("use_your_head1.gif", fps=10, fuzz=2)

