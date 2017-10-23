import sys,os,time

def print_ch_by_ch(text,wait):
    full_text=""
    for ch in text:
        full_text="{0}{1}".format(full_text, ch)
        print(full_text)
        time.sleep(wait)
        os.system('cls')

tex="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam volutpat pellentesque lorem, at dictum nunc" \
          " tincidunt sit amet. Duis gravida velit vestibulum tincidunt hendrerit. Pellentesque habitant morbi " \
          "tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque eget erat quis mi gravida " \
          "feugiat. Aenean nunc risus, sodales et ante in, euismod scelerisque nulla. Phasellus fringilla nulla ut ante" \
          " luctus egestas lobortis vitae ex. Interdum et malesuada fames ac ante ipsum primis in faucibus. " \
          "Nulla hendrerit ligula et nisi consequat suscipit. Pellentesque lobortis elit quam, sit amet mollis " \
          "tellus lacinia vitae. Nam sit amet nisi ut sapien tempor imperdiet. Suspendisse at sem quam. Donec " \
          "fermentum non neque vitae interdum. Vivamus mollis scelerisque nisl, non egestas mauris iaculis nec." \
          "Suspendisse mollis consectetur porta. Integer sodales felis ac dolor vestibulum, a rutrum eros vulputate." \
          " Etiam ut fermentum tellus. Aenean condimentum sed nisl vitae dapibus. Vestibulum iaculis iaculis est. Sed" \
          " ut lacus et sapien fermentum imperdiet. Integer et velit quis elit sagittis aliquet. Ut vehicula pretium" \
          " eros ac mattis. Sed viverra, lorem eget ullamcorper ultrices, eros tortor molestie velit, eu suscipit" \
          " lacus eros vitae velit. Curabitur molestie nisl efficitur malesuada semper. Aenean id convallis libero." \
          " Nullam aliquet dictum erat sed iaculis. Morbi mi mi, tempus a nulla et, congue viverra lectus.Praesent " \
          "et faucibus urna. Etiam mollis a eros ac eleifend. Maecenas velit mauris, pulvinar eu augue nec, tempor " \
          "rhoncus quam. Quisque non fermentum nisl. Nam lorem magna, tristique id ligula et, consequat posuere " \
          "lacus. Etiam non iaculis "
print_ch_by_ch(tex,0.01)
