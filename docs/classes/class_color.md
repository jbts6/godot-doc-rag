github_url
hide

# Color

A color represented in RGBA format.

classref-introduction-group

## Description

A color represented in RGBA format by a red (`r<class_Color_property_r>`), green (`g<class_Color_property_g>`), blue (`b<class_Color_property_b>`), and alpha (`a<class_Color_property_a>`) component. Each component is a 32-bit floating-point value, usually ranging from `0.0` to `1.0`. Some properties (such as `CanvasItem.modulate<class_CanvasItem_property_modulate>`) may support values greater than `1.0`, for overbright or HDR (High Dynamic Range) colors.

Colors can be created in a number of ways: By the various **Color** constructors, by static methods such as `from_hsv()<class_Color_method_from_hsv>`, and by using a name from the set of standardized colors based on [X11 color names](https://en.wikipedia.org/wiki/X11_color_names) with the addition of `TRANSPARENT<class_Color_constant_TRANSPARENT>`.

[Color constants cheatsheet](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/color_constants.png)

Although **Color** may be used to store values of any encoding, the red (`r<class_Color_property_r>`), green (`g<class_Color_property_g>`), and blue (`b<class_Color_property_b>`) properties of **Color** are expected by Godot to be encoded using the [nonlinear sRGB transfer function](https://en.wikipedia.org/wiki/SRGB#Transfer_function_(%22gamma%22)) unless otherwise stated. This color encoding is used by many traditional art and web tools, making it easy to match colors between Godot and these tools. Godot uses [Rec. ITU-R BT.709](https://en.wikipedia.org/wiki/Rec._709) color primaries, which are used by the sRGB standard.

All physical simulation, such as lighting calculations, and colorimetry transformations, such as `get_luminance()<class_Color_method_get_luminance>`, must be performed on linearly encoded values to produce correct results. When performing these calculations, convert **Color** to and from linear encoding using `srgb_to_linear()<class_Color_method_srgb_to_linear>` and `linear_to_srgb()<class_Color_method_linear_to_srgb>`.

**Note:** In a boolean context, a Color will evaluate to `false` if it is equal to `Color(0, 0, 0, 1)` (opaque black). Otherwise, a Color will always evaluate to `true`.

> [!NOTE]
> There are notable differences when using this API with C#. See `doc_c_sharp_differences` for more information.

classref-introduction-group

## Tutorials

- [2D GD Paint Demo](https://godotengine.org/asset-library/asset/2768)
- [Tween Interpolation Demo](https://godotengine.org/asset-library/asset/2733)
- [GUI Drag And Drop Demo](https://godotengine.org/asset-library/asset/2767)

classref-reftable-group

## Properties

classref-reftable-group

## Constructors

classref-reftable-group

## Methods

classref-reftable-group

## Operators

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**ALICE_BLUE** = `Color(0.9411765, 0.972549, 1, 1)` `🔗<class_Color_constant_ALICE_BLUE>`

Alice blue color.

classref-constant

**ANTIQUE_WHITE** = `Color(0.98039216, 0.92156863, 0.84313726, 1)` `🔗<class_Color_constant_ANTIQUE_WHITE>`

Antique white color.

classref-constant

**AQUA** = `Color(0, 1, 1, 1)` `🔗<class_Color_constant_AQUA>`

Aqua color.

classref-constant

**AQUAMARINE** = `Color(0.49803922, 1, 0.83137256, 1)` `🔗<class_Color_constant_AQUAMARINE>`

Aquamarine color.

classref-constant

**AZURE** = `Color(0.9411765, 1, 1, 1)` `🔗<class_Color_constant_AZURE>`

Azure color.

classref-constant

**BEIGE** = `Color(0.9607843, 0.9607843, 0.8627451, 1)` `🔗<class_Color_constant_BEIGE>`

Beige color.

classref-constant

**BISQUE** = `Color(1, 0.89411765, 0.76862746, 1)` `🔗<class_Color_constant_BISQUE>`

Bisque color.

classref-constant

**BLACK** = `Color(0, 0, 0, 1)` `🔗<class_Color_constant_BLACK>`

Black color. In GDScript, this is the default value of any color.

classref-constant

**BLANCHED_ALMOND** = `Color(1, 0.92156863, 0.8039216, 1)` `🔗<class_Color_constant_BLANCHED_ALMOND>`

Blanched almond color.

classref-constant

**BLUE** = `Color(0, 0, 1, 1)` `🔗<class_Color_constant_BLUE>`

Blue color.

classref-constant

**BLUE_VIOLET** = `Color(0.5411765, 0.16862746, 0.8862745, 1)` `🔗<class_Color_constant_BLUE_VIOLET>`

Blue violet color.

classref-constant

**BROWN** = `Color(0.64705884, 0.16470589, 0.16470589, 1)` `🔗<class_Color_constant_BROWN>`

Brown color.

classref-constant

**BURLYWOOD** = `Color(0.87058824, 0.72156864, 0.5294118, 1)` `🔗<class_Color_constant_BURLYWOOD>`

Burlywood color.

classref-constant

**CADET_BLUE** = `Color(0.37254903, 0.61960787, 0.627451, 1)` `🔗<class_Color_constant_CADET_BLUE>`

Cadet blue color.

classref-constant

**CHARTREUSE** = `Color(0.49803922, 1, 0, 1)` `🔗<class_Color_constant_CHARTREUSE>`

Chartreuse color.

classref-constant

**CHOCOLATE** = `Color(0.8235294, 0.4117647, 0.11764706, 1)` `🔗<class_Color_constant_CHOCOLATE>`

Chocolate color.

classref-constant

**CORAL** = `Color(1, 0.49803922, 0.3137255, 1)` `🔗<class_Color_constant_CORAL>`

Coral color.

classref-constant

**CORNFLOWER_BLUE** = `Color(0.39215687, 0.58431375, 0.92941177, 1)` `🔗<class_Color_constant_CORNFLOWER_BLUE>`

Cornflower blue color.

classref-constant

**CORNSILK** = `Color(1, 0.972549, 0.8627451, 1)` `🔗<class_Color_constant_CORNSILK>`

Cornsilk color.

classref-constant

**CRIMSON** = `Color(0.8627451, 0.078431375, 0.23529412, 1)` `🔗<class_Color_constant_CRIMSON>`

Crimson color.

classref-constant

**CYAN** = `Color(0, 1, 1, 1)` `🔗<class_Color_constant_CYAN>`

Cyan color.

classref-constant

**DARK_BLUE** = `Color(0, 0, 0.54509807, 1)` `🔗<class_Color_constant_DARK_BLUE>`

Dark blue color.

classref-constant

**DARK_CYAN** = `Color(0, 0.54509807, 0.54509807, 1)` `🔗<class_Color_constant_DARK_CYAN>`

Dark cyan color.

classref-constant

**DARK_GOLDENROD** = `Color(0.72156864, 0.5254902, 0.043137256, 1)` `🔗<class_Color_constant_DARK_GOLDENROD>`

Dark goldenrod color.

classref-constant

**DARK_GRAY** = `Color(0.6627451, 0.6627451, 0.6627451, 1)` `🔗<class_Color_constant_DARK_GRAY>`

Dark gray color.

classref-constant

**DARK_GREEN** = `Color(0, 0.39215687, 0, 1)` `🔗<class_Color_constant_DARK_GREEN>`

Dark green color.

classref-constant

**DARK_KHAKI** = `Color(0.7411765, 0.7176471, 0.41960785, 1)` `🔗<class_Color_constant_DARK_KHAKI>`

Dark khaki color.

classref-constant

**DARK_MAGENTA** = `Color(0.54509807, 0, 0.54509807, 1)` `🔗<class_Color_constant_DARK_MAGENTA>`

Dark magenta color.

classref-constant

**DARK_OLIVE_GREEN** = `Color(0.33333334, 0.41960785, 0.18431373, 1)` `🔗<class_Color_constant_DARK_OLIVE_GREEN>`

Dark olive green color.

classref-constant

**DARK_ORANGE** = `Color(1, 0.54901963, 0, 1)` `🔗<class_Color_constant_DARK_ORANGE>`

Dark orange color.

classref-constant

**DARK_ORCHID** = `Color(0.6, 0.19607843, 0.8, 1)` `🔗<class_Color_constant_DARK_ORCHID>`

Dark orchid color.

classref-constant

**DARK_RED** = `Color(0.54509807, 0, 0, 1)` `🔗<class_Color_constant_DARK_RED>`

Dark red color.

classref-constant

**DARK_SALMON** = `Color(0.9137255, 0.5882353, 0.47843137, 1)` `🔗<class_Color_constant_DARK_SALMON>`

Dark salmon color.

classref-constant

**DARK_SEA_GREEN** = `Color(0.56078434, 0.7372549, 0.56078434, 1)` `🔗<class_Color_constant_DARK_SEA_GREEN>`

Dark sea green color.

classref-constant

**DARK_SLATE_BLUE** = `Color(0.28235295, 0.23921569, 0.54509807, 1)` `🔗<class_Color_constant_DARK_SLATE_BLUE>`

Dark slate blue color.

classref-constant

**DARK_SLATE_GRAY** = `Color(0.18431373, 0.30980393, 0.30980393, 1)` `🔗<class_Color_constant_DARK_SLATE_GRAY>`

Dark slate gray color.

classref-constant

**DARK_TURQUOISE** = `Color(0, 0.80784315, 0.81960785, 1)` `🔗<class_Color_constant_DARK_TURQUOISE>`

Dark turquoise color.

classref-constant

**DARK_VIOLET** = `Color(0.5803922, 0, 0.827451, 1)` `🔗<class_Color_constant_DARK_VIOLET>`

Dark violet color.

classref-constant

**DEEP_PINK** = `Color(1, 0.078431375, 0.5764706, 1)` `🔗<class_Color_constant_DEEP_PINK>`

Deep pink color.

classref-constant

**DEEP_SKY_BLUE** = `Color(0, 0.7490196, 1, 1)` `🔗<class_Color_constant_DEEP_SKY_BLUE>`

Deep sky blue color.

classref-constant

**DIM_GRAY** = `Color(0.4117647, 0.4117647, 0.4117647, 1)` `🔗<class_Color_constant_DIM_GRAY>`

Dim gray color.

classref-constant

**DODGER_BLUE** = `Color(0.11764706, 0.5647059, 1, 1)` `🔗<class_Color_constant_DODGER_BLUE>`

Dodger blue color.

classref-constant

**FIREBRICK** = `Color(0.69803923, 0.13333334, 0.13333334, 1)` `🔗<class_Color_constant_FIREBRICK>`

Firebrick color.

classref-constant

**FLORAL_WHITE** = `Color(1, 0.98039216, 0.9411765, 1)` `🔗<class_Color_constant_FLORAL_WHITE>`

Floral white color.

classref-constant

**FOREST_GREEN** = `Color(0.13333334, 0.54509807, 0.13333334, 1)` `🔗<class_Color_constant_FOREST_GREEN>`

Forest green color.

classref-constant

**FUCHSIA** = `Color(1, 0, 1, 1)` `🔗<class_Color_constant_FUCHSIA>`

Fuchsia color.

classref-constant

**GAINSBORO** = `Color(0.8627451, 0.8627451, 0.8627451, 1)` `🔗<class_Color_constant_GAINSBORO>`

Gainsboro color.

classref-constant

**GHOST_WHITE** = `Color(0.972549, 0.972549, 1, 1)` `🔗<class_Color_constant_GHOST_WHITE>`

Ghost white color.

classref-constant

**GOLD** = `Color(1, 0.84313726, 0, 1)` `🔗<class_Color_constant_GOLD>`

Gold color.

classref-constant

**GOLDENROD** = `Color(0.85490197, 0.64705884, 0.1254902, 1)` `🔗<class_Color_constant_GOLDENROD>`

Goldenrod color.

classref-constant

**GRAY** = `Color(0.74509805, 0.74509805, 0.74509805, 1)` `🔗<class_Color_constant_GRAY>`

Gray color.

classref-constant

**GREEN** = `Color(0, 1, 0, 1)` `🔗<class_Color_constant_GREEN>`

Green color.

classref-constant

**GREEN_YELLOW** = `Color(0.6784314, 1, 0.18431373, 1)` `🔗<class_Color_constant_GREEN_YELLOW>`

Green yellow color.

classref-constant

**HONEYDEW** = `Color(0.9411765, 1, 0.9411765, 1)` `🔗<class_Color_constant_HONEYDEW>`

Honeydew color.

classref-constant

**HOT_PINK** = `Color(1, 0.4117647, 0.7058824, 1)` `🔗<class_Color_constant_HOT_PINK>`

Hot pink color.

classref-constant

**INDIAN_RED** = `Color(0.8039216, 0.36078432, 0.36078432, 1)` `🔗<class_Color_constant_INDIAN_RED>`

Indian red color.

classref-constant

**INDIGO** = `Color(0.29411766, 0, 0.50980395, 1)` `🔗<class_Color_constant_INDIGO>`

Indigo color.

classref-constant

**IVORY** = `Color(1, 1, 0.9411765, 1)` `🔗<class_Color_constant_IVORY>`

Ivory color.

classref-constant

**KHAKI** = `Color(0.9411765, 0.9019608, 0.54901963, 1)` `🔗<class_Color_constant_KHAKI>`

Khaki color.

classref-constant

**LAVENDER** = `Color(0.9019608, 0.9019608, 0.98039216, 1)` `🔗<class_Color_constant_LAVENDER>`

Lavender color.

classref-constant

**LAVENDER_BLUSH** = `Color(1, 0.9411765, 0.9607843, 1)` `🔗<class_Color_constant_LAVENDER_BLUSH>`

Lavender blush color.

classref-constant

**LAWN_GREEN** = `Color(0.4862745, 0.9882353, 0, 1)` `🔗<class_Color_constant_LAWN_GREEN>`

Lawn green color.

classref-constant

**LEMON_CHIFFON** = `Color(1, 0.98039216, 0.8039216, 1)` `🔗<class_Color_constant_LEMON_CHIFFON>`

Lemon chiffon color.

classref-constant

**LIGHT_BLUE** = `Color(0.6784314, 0.84705883, 0.9019608, 1)` `🔗<class_Color_constant_LIGHT_BLUE>`

Light blue color.

classref-constant

**LIGHT_CORAL** = `Color(0.9411765, 0.5019608, 0.5019608, 1)` `🔗<class_Color_constant_LIGHT_CORAL>`

Light coral color.

classref-constant

**LIGHT_CYAN** = `Color(0.8784314, 1, 1, 1)` `🔗<class_Color_constant_LIGHT_CYAN>`

Light cyan color.

classref-constant

**LIGHT_GOLDENROD** = `Color(0.98039216, 0.98039216, 0.8235294, 1)` `🔗<class_Color_constant_LIGHT_GOLDENROD>`

Light goldenrod color.

classref-constant

**LIGHT_GRAY** = `Color(0.827451, 0.827451, 0.827451, 1)` `🔗<class_Color_constant_LIGHT_GRAY>`

Light gray color.

classref-constant

**LIGHT_GREEN** = `Color(0.5647059, 0.93333334, 0.5647059, 1)` `🔗<class_Color_constant_LIGHT_GREEN>`

Light green color.

classref-constant

**LIGHT_PINK** = `Color(1, 0.7137255, 0.75686276, 1)` `🔗<class_Color_constant_LIGHT_PINK>`

Light pink color.

classref-constant

**LIGHT_SALMON** = `Color(1, 0.627451, 0.47843137, 1)` `🔗<class_Color_constant_LIGHT_SALMON>`

Light salmon color.

classref-constant

**LIGHT_SEA_GREEN** = `Color(0.1254902, 0.69803923, 0.6666667, 1)` `🔗<class_Color_constant_LIGHT_SEA_GREEN>`

Light sea green color.

classref-constant

**LIGHT_SKY_BLUE** = `Color(0.5294118, 0.80784315, 0.98039216, 1)` `🔗<class_Color_constant_LIGHT_SKY_BLUE>`

Light sky blue color.

classref-constant

**LIGHT_SLATE_GRAY** = `Color(0.46666667, 0.53333336, 0.6, 1)` `🔗<class_Color_constant_LIGHT_SLATE_GRAY>`

Light slate gray color.

classref-constant

**LIGHT_STEEL_BLUE** = `Color(0.6901961, 0.76862746, 0.87058824, 1)` `🔗<class_Color_constant_LIGHT_STEEL_BLUE>`

Light steel blue color.

classref-constant

**LIGHT_YELLOW** = `Color(1, 1, 0.8784314, 1)` `🔗<class_Color_constant_LIGHT_YELLOW>`

Light yellow color.

classref-constant

**LIME** = `Color(0, 1, 0, 1)` `🔗<class_Color_constant_LIME>`

Lime color.

classref-constant

**LIME_GREEN** = `Color(0.19607843, 0.8039216, 0.19607843, 1)` `🔗<class_Color_constant_LIME_GREEN>`

Lime green color.

classref-constant

**LINEN** = `Color(0.98039216, 0.9411765, 0.9019608, 1)` `🔗<class_Color_constant_LINEN>`

Linen color.

classref-constant

**MAGENTA** = `Color(1, 0, 1, 1)` `🔗<class_Color_constant_MAGENTA>`

Magenta color.

classref-constant

**MAROON** = `Color(0.6901961, 0.1882353, 0.3764706, 1)` `🔗<class_Color_constant_MAROON>`

Maroon color.

classref-constant

**MEDIUM_AQUAMARINE** = `Color(0.4, 0.8039216, 0.6666667, 1)` `🔗<class_Color_constant_MEDIUM_AQUAMARINE>`

Medium aquamarine color.

classref-constant

**MEDIUM_BLUE** = `Color(0, 0, 0.8039216, 1)` `🔗<class_Color_constant_MEDIUM_BLUE>`

Medium blue color.

classref-constant

**MEDIUM_ORCHID** = `Color(0.7294118, 0.33333334, 0.827451, 1)` `🔗<class_Color_constant_MEDIUM_ORCHID>`

Medium orchid color.

classref-constant

**MEDIUM_PURPLE** = `Color(0.5764706, 0.4392157, 0.85882354, 1)` `🔗<class_Color_constant_MEDIUM_PURPLE>`

Medium purple color.

classref-constant

**MEDIUM_SEA_GREEN** = `Color(0.23529412, 0.7019608, 0.44313726, 1)` `🔗<class_Color_constant_MEDIUM_SEA_GREEN>`

Medium sea green color.

classref-constant

**MEDIUM_SLATE_BLUE** = `Color(0.48235294, 0.40784314, 0.93333334, 1)` `🔗<class_Color_constant_MEDIUM_SLATE_BLUE>`

Medium slate blue color.

classref-constant

**MEDIUM_SPRING_GREEN** = `Color(0, 0.98039216, 0.6039216, 1)` `🔗<class_Color_constant_MEDIUM_SPRING_GREEN>`

Medium spring green color.

classref-constant

**MEDIUM_TURQUOISE** = `Color(0.28235295, 0.81960785, 0.8, 1)` `🔗<class_Color_constant_MEDIUM_TURQUOISE>`

Medium turquoise color.

classref-constant

**MEDIUM_VIOLET_RED** = `Color(0.78039217, 0.08235294, 0.52156866, 1)` `🔗<class_Color_constant_MEDIUM_VIOLET_RED>`

Medium violet red color.

classref-constant

**MIDNIGHT_BLUE** = `Color(0.09803922, 0.09803922, 0.4392157, 1)` `🔗<class_Color_constant_MIDNIGHT_BLUE>`

Midnight blue color.

classref-constant

**MINT_CREAM** = `Color(0.9607843, 1, 0.98039216, 1)` `🔗<class_Color_constant_MINT_CREAM>`

Mint cream color.

classref-constant

**MISTY_ROSE** = `Color(1, 0.89411765, 0.88235295, 1)` `🔗<class_Color_constant_MISTY_ROSE>`

Misty rose color.

classref-constant

**MOCCASIN** = `Color(1, 0.89411765, 0.70980394, 1)` `🔗<class_Color_constant_MOCCASIN>`

Moccasin color.

classref-constant

**NAVAJO_WHITE** = `Color(1, 0.87058824, 0.6784314, 1)` `🔗<class_Color_constant_NAVAJO_WHITE>`

Navajo white color.

classref-constant

**NAVY_BLUE** = `Color(0, 0, 0.5019608, 1)` `🔗<class_Color_constant_NAVY_BLUE>`

Navy blue color.

classref-constant

**OLD_LACE** = `Color(0.99215686, 0.9607843, 0.9019608, 1)` `🔗<class_Color_constant_OLD_LACE>`

Old lace color.

classref-constant

**OLIVE** = `Color(0.5019608, 0.5019608, 0, 1)` `🔗<class_Color_constant_OLIVE>`

Olive color.

classref-constant

**OLIVE_DRAB** = `Color(0.41960785, 0.5568628, 0.13725491, 1)` `🔗<class_Color_constant_OLIVE_DRAB>`

Olive drab color.

classref-constant

**ORANGE** = `Color(1, 0.64705884, 0, 1)` `🔗<class_Color_constant_ORANGE>`

Orange color.

classref-constant

**ORANGE_RED** = `Color(1, 0.27058825, 0, 1)` `🔗<class_Color_constant_ORANGE_RED>`

Orange red color.

classref-constant

**ORCHID** = `Color(0.85490197, 0.4392157, 0.8392157, 1)` `🔗<class_Color_constant_ORCHID>`

Orchid color.

classref-constant

**PALE_GOLDENROD** = `Color(0.93333334, 0.9098039, 0.6666667, 1)` `🔗<class_Color_constant_PALE_GOLDENROD>`

Pale goldenrod color.

classref-constant

**PALE_GREEN** = `Color(0.59607846, 0.9843137, 0.59607846, 1)` `🔗<class_Color_constant_PALE_GREEN>`

Pale green color.

classref-constant

**PALE_TURQUOISE** = `Color(0.6862745, 0.93333334, 0.93333334, 1)` `🔗<class_Color_constant_PALE_TURQUOISE>`

Pale turquoise color.

classref-constant

**PALE_VIOLET_RED** = `Color(0.85882354, 0.4392157, 0.5764706, 1)` `🔗<class_Color_constant_PALE_VIOLET_RED>`

Pale violet red color.

classref-constant

**PAPAYA_WHIP** = `Color(1, 0.9372549, 0.8352941, 1)` `🔗<class_Color_constant_PAPAYA_WHIP>`

Papaya whip color.

classref-constant

**PEACH_PUFF** = `Color(1, 0.85490197, 0.7254902, 1)` `🔗<class_Color_constant_PEACH_PUFF>`

Peach puff color.

classref-constant

**PERU** = `Color(0.8039216, 0.52156866, 0.24705882, 1)` `🔗<class_Color_constant_PERU>`

Peru color.

classref-constant

**PINK** = `Color(1, 0.7529412, 0.79607844, 1)` `🔗<class_Color_constant_PINK>`

Pink color.

classref-constant

**PLUM** = `Color(0.8666667, 0.627451, 0.8666667, 1)` `🔗<class_Color_constant_PLUM>`

Plum color.

classref-constant

**POWDER_BLUE** = `Color(0.6901961, 0.8784314, 0.9019608, 1)` `🔗<class_Color_constant_POWDER_BLUE>`

Powder blue color.

classref-constant

**PURPLE** = `Color(0.627451, 0.1254902, 0.9411765, 1)` `🔗<class_Color_constant_PURPLE>`

Purple color.

classref-constant

**REBECCA_PURPLE** = `Color(0.4, 0.2, 0.6, 1)` `🔗<class_Color_constant_REBECCA_PURPLE>`

Rebecca purple color.

classref-constant

**RED** = `Color(1, 0, 0, 1)` `🔗<class_Color_constant_RED>`

Red color.

classref-constant

**ROSY_BROWN** = `Color(0.7372549, 0.56078434, 0.56078434, 1)` `🔗<class_Color_constant_ROSY_BROWN>`

Rosy brown color.

classref-constant

**ROYAL_BLUE** = `Color(0.25490198, 0.4117647, 0.88235295, 1)` `🔗<class_Color_constant_ROYAL_BLUE>`

Royal blue color.

classref-constant

**SADDLE_BROWN** = `Color(0.54509807, 0.27058825, 0.07450981, 1)` `🔗<class_Color_constant_SADDLE_BROWN>`

Saddle brown color.

classref-constant

**SALMON** = `Color(0.98039216, 0.5019608, 0.44705883, 1)` `🔗<class_Color_constant_SALMON>`

Salmon color.

classref-constant

**SANDY_BROWN** = `Color(0.95686275, 0.6431373, 0.3764706, 1)` `🔗<class_Color_constant_SANDY_BROWN>`

Sandy brown color.

classref-constant

**SEA_GREEN** = `Color(0.18039216, 0.54509807, 0.34117648, 1)` `🔗<class_Color_constant_SEA_GREEN>`

Sea green color.

classref-constant

**SEASHELL** = `Color(1, 0.9607843, 0.93333334, 1)` `🔗<class_Color_constant_SEASHELL>`

Seashell color.

classref-constant

**SIENNA** = `Color(0.627451, 0.32156864, 0.1764706, 1)` `🔗<class_Color_constant_SIENNA>`

Sienna color.

classref-constant

**SILVER** = `Color(0.7529412, 0.7529412, 0.7529412, 1)` `🔗<class_Color_constant_SILVER>`

Silver color.

classref-constant

**SKY_BLUE** = `Color(0.5294118, 0.80784315, 0.92156863, 1)` `🔗<class_Color_constant_SKY_BLUE>`

Sky blue color.

classref-constant

**SLATE_BLUE** = `Color(0.41568628, 0.3529412, 0.8039216, 1)` `🔗<class_Color_constant_SLATE_BLUE>`

Slate blue color.

classref-constant

**SLATE_GRAY** = `Color(0.4392157, 0.5019608, 0.5647059, 1)` `🔗<class_Color_constant_SLATE_GRAY>`

Slate gray color.

classref-constant

**SNOW** = `Color(1, 0.98039216, 0.98039216, 1)` `🔗<class_Color_constant_SNOW>`

Snow color.

classref-constant

**SPRING_GREEN** = `Color(0, 1, 0.49803922, 1)` `🔗<class_Color_constant_SPRING_GREEN>`

Spring green color.

classref-constant

**STEEL_BLUE** = `Color(0.27450982, 0.50980395, 0.7058824, 1)` `🔗<class_Color_constant_STEEL_BLUE>`

Steel blue color.

classref-constant

**TAN** = `Color(0.8235294, 0.7058824, 0.54901963, 1)` `🔗<class_Color_constant_TAN>`

Tan color.

classref-constant

**TEAL** = `Color(0, 0.5019608, 0.5019608, 1)` `🔗<class_Color_constant_TEAL>`

Teal color.

classref-constant

**THISTLE** = `Color(0.84705883, 0.7490196, 0.84705883, 1)` `🔗<class_Color_constant_THISTLE>`

Thistle color.

classref-constant

**TOMATO** = `Color(1, 0.3882353, 0.2784314, 1)` `🔗<class_Color_constant_TOMATO>`

Tomato color.

classref-constant

**TRANSPARENT** = `Color(1, 1, 1, 0)` `🔗<class_Color_constant_TRANSPARENT>`

Transparent color (white with zero alpha).

classref-constant

**TURQUOISE** = `Color(0.2509804, 0.8784314, 0.8156863, 1)` `🔗<class_Color_constant_TURQUOISE>`

Turquoise color.

classref-constant

**VIOLET** = `Color(0.93333334, 0.50980395, 0.93333334, 1)` `🔗<class_Color_constant_VIOLET>`

Violet color.

classref-constant

**WEB_GRAY** = `Color(0.5019608, 0.5019608, 0.5019608, 1)` `🔗<class_Color_constant_WEB_GRAY>`

Web gray color.

classref-constant

**WEB_GREEN** = `Color(0, 0.5019608, 0, 1)` `🔗<class_Color_constant_WEB_GREEN>`

Web green color.

classref-constant

**WEB_MAROON** = `Color(0.5019608, 0, 0, 1)` `🔗<class_Color_constant_WEB_MAROON>`

Web maroon color.

classref-constant

**WEB_PURPLE** = `Color(0.5019608, 0, 0.5019608, 1)` `🔗<class_Color_constant_WEB_PURPLE>`

Web purple color.

classref-constant

**WHEAT** = `Color(0.9607843, 0.87058824, 0.7019608, 1)` `🔗<class_Color_constant_WHEAT>`

Wheat color.

classref-constant

**WHITE** = `Color(1, 1, 1, 1)` `🔗<class_Color_constant_WHITE>`

White color.

classref-constant

**WHITE_SMOKE** = `Color(0.9607843, 0.9607843, 0.9607843, 1)` `🔗<class_Color_constant_WHITE_SMOKE>`

White smoke color.

classref-constant

**YELLOW** = `Color(1, 1, 0, 1)` `🔗<class_Color_constant_YELLOW>`

Yellow color.

classref-constant

**YELLOW_GREEN** = `Color(0.6039216, 0.8039216, 0.19607843, 1)` `🔗<class_Color_constant_YELLOW_GREEN>`

Yellow green color.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **a** = `1.0` `🔗<class_Color_property_a>`

The color's alpha component, typically on the range of 0 to 1. A value of 0 means that the color is fully transparent. A value of 1 means that the color is fully opaque.

**Note:** The alpha channel is always stored with linear encoding, regardless of the encoding of the other color channels. The `linear_to_srgb()<class_Color_method_linear_to_srgb>` and `srgb_to_linear()<class_Color_method_srgb_to_linear>` methods do not affect the alpha channel.

classref-item-separator

classref-property

`int<class_int>` **a8** = `255` `🔗<class_Color_property_a8>`

Wrapper for `a<class_Color_property_a>` that uses the range 0 to 255, instead of 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **b** = `0.0` `🔗<class_Color_property_b>`

The color's blue component, typically on the range of 0 to 1.

classref-item-separator

classref-property

`int<class_int>` **b8** = `0` `🔗<class_Color_property_b8>`

Wrapper for `b<class_Color_property_b>` that uses the range 0 to 255, instead of 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **g** = `0.0` `🔗<class_Color_property_g>`

The color's green component, typically on the range of 0 to 1.

classref-item-separator

classref-property

`int<class_int>` **g8** = `0` `🔗<class_Color_property_g8>`

Wrapper for `g<class_Color_property_g>` that uses the range 0 to 255, instead of 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **h** = `0.0` `🔗<class_Color_property_h>`

The HSV hue of this color, on the range 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **ok_hsl_h** = `0.0` `🔗<class_Color_property_ok_hsl_h>`

The OKHSL hue of this color, on the range 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **ok_hsl_l** = `0.0` `🔗<class_Color_property_ok_hsl_l>`

The OKHSL lightness of this color, on the range 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **ok_hsl_s** = `0.0` `🔗<class_Color_property_ok_hsl_s>`

The OKHSL saturation of this color, on the range 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **r** = `0.0` `🔗<class_Color_property_r>`

The color's red component, typically on the range of 0 to 1.

classref-item-separator

classref-property

`int<class_int>` **r8** = `0` `🔗<class_Color_property_r8>`

Wrapper for `r<class_Color_property_r>` that uses the range 0 to 255, instead of 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **s** = `0.0` `🔗<class_Color_property_s>`

The HSV saturation of this color, on the range 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **v** = `0.0` `🔗<class_Color_property_v>`

The HSV value (brightness) of this color, on the range 0 to 1.

classref-section-separator

classref-descriptions-group

## Constructor Descriptions

classref-constructor

`Color<class_Color>` **Color**() `🔗<class_Color_constructor_Color>`

Constructs a default **Color** from opaque black. This is the same as `BLACK<class_Color_constant_BLACK>`.

**Note:** In C#, this constructs a **Color** with all of its components set to `0.0` (transparent black).

classref-item-separator

classref-constructor

`Color<class_Color>` **Color**(from: `Color<class_Color>`, alpha: `float<class_float>`)

Constructs a **Color** from the existing color, with `a<class_Color_property_a>` set to the given `alpha` value.

gdscript

var red = Color(Color.RED, 0.2) \# 20% opaque red.

csharp

var red = new Color(Colors.Red, 0.2f); // 20% opaque red.

classref-item-separator

classref-constructor

`Color<class_Color>` **Color**(from: `Color<class_Color>`)

Constructs a **Color** as a copy of the given **Color**.

classref-item-separator

classref-constructor

`Color<class_Color>` **Color**(code: `String<class_String>`)

Constructs a **Color** either from an HTML color code or from a standardized color name. The supported color names are the same as the constants.

classref-item-separator

classref-constructor

`Color<class_Color>` **Color**(code: `String<class_String>`, alpha: `float<class_float>`)

Constructs a **Color** either from an HTML color code or from a standardized color name, with `alpha` on the range of 0.0 to 1.0. The supported color names are the same as the constants.

classref-item-separator

classref-constructor

`Color<class_Color>` **Color**(r: `float<class_float>`, g: `float<class_float>`, b: `float<class_float>`)

Constructs a **Color** from RGB values, typically between 0.0 and 1.0. `a<class_Color_property_a>` is set to 1.0.

gdscript

var color = Color(0.2, 1.0, 0.7) \# Similar to Color.from_rgba8(51, 255, 178, 255)

csharp

var color = new Color(0.2f, 1.0f, 0.7f); // Similar to Color.Color8(51, 255, 178, 255)

classref-item-separator

classref-constructor

`Color<class_Color>` **Color**(r: `float<class_float>`, g: `float<class_float>`, b: `float<class_float>`, a: `float<class_float>`)

Constructs a **Color** from RGBA values, typically between 0.0 and 1.0.

gdscript

var color = Color(0.2, 1.0, 0.7, 0.8) \# Similar to Color.from_rgba8(51, 255, 178, 204)

csharp

var color = new Color(0.2f, 1.0f, 0.7f, 0.8f); // Similar to Color.Color8(51, 255, 178, 255, 204)

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Color<class_Color>` **blend**(over: `Color<class_Color>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_blend>`

Returns a new color resulting from overlaying this color over the given color. In a painting program, you can imagine it as the `over` color painted over this color (including alpha).

gdscript

var bg = Color(0.0, 1.0, 0.0, 0.5) \# Green with alpha of 50% var fg = Color(1.0, 0.0, 0.0, 0.5) \# Red with alpha of 50% var blended_color = bg.blend(fg) \# Brown with alpha of 75%

csharp

var bg = new Color(0.0f, 1.0f, 0.0f, 0.5f); // Green with alpha of 50% var fg = new Color(1.0f, 0.0f, 0.0f, 0.5f); // Red with alpha of 50% Color blendedColor = bg.Blend(fg); // Brown with alpha of 75%

classref-item-separator

classref-method

`Color<class_Color>` **clamp**(min: `Color<class_Color>` = Color(0, 0, 0, 0), max: `Color<class_Color>` = Color(1, 1, 1, 1)) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_clamp>`

Returns a new color with all components clamped between the components of `min` and `max`, by running `@GlobalScope.clamp()<class_@GlobalScope_method_clamp>` on each component.

classref-item-separator

classref-method

`Color<class_Color>` **darkened**(amount: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_darkened>`

Returns a new color resulting from making this color darker by the specified `amount` (ratio from 0.0 to 1.0). See also `lightened()<class_Color_method_lightened>`.

gdscript

var green = Color(0.0, 1.0, 0.0) var darkgreen = green.darkened(0.2) \# 20% darker than regular green

csharp

var green = new Color(0.0f, 1.0f, 0.0f); Color darkgreen = green.Darkened(0.2f); // 20% darker than regular green

classref-item-separator

classref-method

`Color<class_Color>` **from_hsv**(h: `float<class_float>`, s: `float<class_float>`, v: `float<class_float>`, alpha: `float<class_float>` = 1.0) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Color_method_from_hsv>`

Constructs a color from an [HSV profile](https://en.wikipedia.org/wiki/HSL_and_HSV). The hue (`h`), saturation (`s`), and value (`v`) are typically between 0.0 and 1.0.

gdscript

var color = Color.from_hsv(0.58, 0.5, 0.79, 0.8)

csharp

var color = Color.FromHsv(0.58f, 0.5f, 0.79f, 0.8f);

classref-item-separator

classref-method

`Color<class_Color>` **from_ok_hsl**(h: `float<class_float>`, s: `float<class_float>`, l: `float<class_float>`, alpha: `float<class_float>` = 1.0) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Color_method_from_ok_hsl>`

Constructs a color from an [OK HSL profile](https://bottosson.github.io/posts/colorpicker/). The hue (`h`), saturation (`s`), and lightness (`l`) are typically between 0.0 and 1.0.

gdscript

var color = Color.from_ok_hsl(0.58, 0.5, 0.79, 0.8)

csharp

var color = Color.FromOkHsl(0.58f, 0.5f, 0.79f, 0.8f);

classref-item-separator

classref-method

`Color<class_Color>` **from_rgba8**(r8: `int<class_int>`, g8: `int<class_int>`, b8: `int<class_int>`, a8: `int<class_int>` = 255) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Color_method_from_rgba8>`

Returns a **Color** constructed from red (`r8`), green (`g8`), blue (`b8`), and optionally alpha (`a8`) integer channels, each divided by `255.0` for their final value.

    var red = Color.from_rgba8(255, 0, 0)             # Same as Color(1, 0, 0).
    var dark_blue = Color.from_rgba8(0, 0, 51)        # Same as Color(0, 0, 0.2).
    var my_color = Color.from_rgba8(306, 255, 0, 102) # Same as Color(1.2, 1, 0, 0.4).

**Note:** Due to the lower precision of `from_rgba8()<class_Color_method_from_rgba8>` compared to the standard **Color** constructor, a color created with `from_rgba8()<class_Color_method_from_rgba8>` will generally not be equal to the same color created with the standard **Color** constructor. Use `is_equal_approx()<class_Color_method_is_equal_approx>` for comparisons to avoid issues with floating-point precision error.

classref-item-separator

classref-method

`Color<class_Color>` **from_rgbe9995**(rgbe: `int<class_int>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Color_method_from_rgbe9995>`

Decodes a **Color** from an RGBE9995 format integer. See `Image.FORMAT_RGBE9995<class_Image_constant_FORMAT_RGBE9995>`.

classref-item-separator

classref-method

`Color<class_Color>` **from_string**(str: `String<class_String>`, default: `Color<class_Color>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Color_method_from_string>`

Creates a **Color** from the given string, which can be either an HTML color code or a named color (case-insensitive). Returns `default` if the color cannot be inferred from the string.

If you want to create a color from String in a constant expression, use the equivalent constructor instead (i.e. `Color("color string")`).

classref-item-separator

classref-method

`float<class_float>` **get_luminance**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_get_luminance>`

Returns the light intensity of the color, as a value between 0.0 and 1.0 (inclusive). This is useful when determining light or dark color. Colors with a luminance smaller than 0.5 can be generally considered dark.

**Note:** `get_luminance()<class_Color_method_get_luminance>` relies on the color using linear encoding to return an accurate relative luminance value. If the color uses the default nonlinear sRGB encoding, use `srgb_to_linear()<class_Color_method_srgb_to_linear>` to convert it to linear encoding first.

classref-item-separator

classref-method

`Color<class_Color>` **hex**(hex: `int<class_int>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Color_method_hex>`

Returns the **Color** associated with the provided `hex` integer in 32-bit RGBA format (8 bits per channel). This method is the inverse of `to_rgba32()<class_Color_method_to_rgba32>`.

In GDScript and C#, the `int<class_int>` is best visualized with hexadecimal notation (`"0x"` prefix, making it `"0xRRGGBBAA"`).

gdscript

var red = Color.hex(0xff0000ff) var dark_cyan = Color.hex(0x008b8bff) var my_color = Color.hex(0xbbefd2a4)

csharp

var red = new Color(0xff0000ff); var dark_cyan = new Color(0x008b8bff); var my_color = new Color(0xbbefd2a4);

If you want to use hex notation in a constant expression, use the equivalent constructor instead (i.e. `Color(0xRRGGBBAA)`).

classref-item-separator

classref-method

`Color<class_Color>` **hex64**(hex: `int<class_int>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Color_method_hex64>`

Returns the **Color** associated with the provided `hex` integer in 64-bit RGBA format (16 bits per channel). This method is the inverse of `to_rgba64()<class_Color_method_to_rgba64>`.

In GDScript and C#, the `int<class_int>` is best visualized with hexadecimal notation (`"0x"` prefix, making it `"0xRRRRGGGGBBBBAAAA"`).

classref-item-separator

classref-method

`Color<class_Color>` **html**(rgba: `String<class_String>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Color_method_html>`

Returns a new color from `rgba`, an HTML hexadecimal color string. `rgba` is not case-sensitive, and may be prefixed by a hash sign (`#`).

`rgba` must be a valid three-digit or six-digit hexadecimal color string, and may contain an alpha channel value. If `rgba` does not contain an alpha channel value, an alpha channel value of 1.0 is applied. If `rgba` is invalid, returns an empty color.

gdscript

var blue = Color.html("#0000ff") \# blue is Color(0.0, 0.0, 1.0, 1.0) var green = Color.html("#0F0") \# green is Color(0.0, 1.0, 0.0, 1.0) var col = Color.html("663399cc") \# col is Color(0.4, 0.2, 0.6, 0.8)

csharp

var blue = Color.FromHtml("#0000ff"); // blue is Color(0.0, 0.0, 1.0, 1.0) var green = Color.FromHtml("#0F0"); // green is Color(0.0, 1.0, 0.0, 1.0) var col = Color.FromHtml("663399cc"); // col is Color(0.4, 0.2, 0.6, 0.8)

classref-item-separator

classref-method

`bool<class_bool>` **html_is_valid**(color: `String<class_String>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Color_method_html_is_valid>`

Returns `true` if `color` is a valid HTML hexadecimal color string. The string must be a hexadecimal value (case-insensitive) of either 3, 4, 6 or 8 digits, and may be prefixed by a hash sign (`#`). This method is identical to `String.is_valid_html_color()<class_String_method_is_valid_html_color>`.

gdscript

Color.html_is_valid("#55aaFF") \# Returns true Color.html_is_valid("#55AAFF20") \# Returns true Color.html_is_valid("55AAFF") \# Returns true Color.html_is_valid("#F2C") \# Returns true

Color.html_is_valid("#AABBC") \# Returns false Color.html_is_valid("#55aaFF5") \# Returns false

csharp

Color.HtmlIsValid("#55AAFF"); // Returns true Color.HtmlIsValid("#55AAFF20"); // Returns true Color.HtmlIsValid("55AAFF"); // Returns true Color.HtmlIsValid("#F2C"); // Returns true

Color.HtmlIsValid("#AABBC"); // Returns false Color.HtmlIsValid("#55aaFF5"); // Returns false

classref-item-separator

classref-method

`Color<class_Color>` **inverted**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_inverted>`

Returns the color with its `r<class_Color_property_r>`, `g<class_Color_property_g>`, and `b<class_Color_property_b>` components inverted (`(1 - r, 1 - g, 1 - b, a)`).

gdscript

var black = Color.WHITE.inverted() var color = Color(0.3, 0.4, 0.9) var inverted_color = color.inverted() \# Equivalent to Color(0.7, 0.6, 0.1)

csharp

var black = Colors.White.Inverted(); var color = new Color(0.3f, 0.4f, 0.9f); Color invertedColor = color.Inverted(); // Equivalent to new Color(0.7f, 0.6f, 0.1f)

classref-item-separator

classref-method

`bool<class_bool>` **is_equal_approx**(to: `Color<class_Color>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_is_equal_approx>`

Returns `true` if this color and `to` are approximately equal, by running `@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>` on each component.

classref-item-separator

classref-method

`Color<class_Color>` **lerp**(to: `Color<class_Color>`, weight: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_lerp>`

Returns the linear interpolation between this color's components and `to`'s components. The interpolation factor `weight` should be between 0.0 and 1.0 (inclusive). See also `@GlobalScope.lerp()<class_@GlobalScope_method_lerp>`.

gdscript

var red = Color(1.0, 0.0, 0.0) var aqua = Color(0.0, 1.0, 0.8)

red.lerp(aqua, 0.2) \# Returns Color(0.8, 0.2, 0.16) red.lerp(aqua, 0.5) \# Returns Color(0.5, 0.5, 0.4) red.lerp(aqua, 1.0) \# Returns Color(0.0, 1.0, 0.8)

csharp

var red = new Color(1.0f, 0.0f, 0.0f); var aqua = new Color(0.0f, 1.0f, 0.8f);

red.Lerp(aqua, 0.2f); // Returns Color(0.8f, 0.2f, 0.16f) red.Lerp(aqua, 0.5f); // Returns Color(0.5f, 0.5f, 0.4f) red.Lerp(aqua, 1.0f); // Returns Color(0.0f, 1.0f, 0.8f)

classref-item-separator

classref-method

`Color<class_Color>` **lightened**(amount: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_lightened>`

Returns a new color resulting from making this color lighter by the specified `amount`, which should be a ratio from 0.0 to 1.0. See also `darkened()<class_Color_method_darkened>`.

gdscript

var green = Color(0.0, 1.0, 0.0) var light_green = green.lightened(0.2) \# 20% lighter than regular green

csharp

var green = new Color(0.0f, 1.0f, 0.0f); Color lightGreen = green.Lightened(0.2f); // 20% lighter than regular green

classref-item-separator

classref-method

`Color<class_Color>` **linear_to_srgb**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_linear_to_srgb>`

Returns a copy of the color that is encoded using the [nonlinear sRGB transfer function](https://en.wikipedia.org/wiki/SRGB). This method requires the original color to use linear encoding. See also `srgb_to_linear()<class_Color_method_srgb_to_linear>` which performs the opposite operation.

**Note:** The color's alpha channel (`a<class_Color_property_a>`) is not affected. The alpha channel is always stored with linear encoding, regardless of the color space of the other color channels.

classref-item-separator

classref-method

`Color<class_Color>` **srgb_to_linear**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_srgb_to_linear>`

Returns a copy of the color that uses linear encoding. This method requires the original color to be encoded using the [nonlinear sRGB transfer function](https://en.wikipedia.org/wiki/SRGB). See also `linear_to_srgb()<class_Color_method_linear_to_srgb>` which performs the opposite operation.

**Note:** The color's alpha channel (`a<class_Color_property_a>`) is not affected. The alpha channel is always stored with linear encoding, regardless of the color space of the other color channels.

classref-item-separator

classref-method

`int<class_int>` **to_abgr32**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_to_abgr32>`

Returns the color converted to a 32-bit integer in ABGR format (each component is 8 bits). ABGR is the reversed version of the default RGBA format.

gdscript

var color = Color(1, 0.5, 0.2) print(color.to_abgr32()) \# Prints 4281565439

csharp

var color = new Color(1.0f, 0.5f, 0.2f); GD.Print(color.ToAbgr32()); // Prints 4281565439

classref-item-separator

classref-method

`int<class_int>` **to_abgr64**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_to_abgr64>`

Returns the color converted to a 64-bit integer in ABGR format (each component is 16 bits). ABGR is the reversed version of the default RGBA format.

gdscript

var color = Color(1, 0.5, 0.2) print(color.to_abgr64()) \# Prints -225178692812801

csharp

var color = new Color(1.0f, 0.5f, 0.2f); GD.Print(color.ToAbgr64()); // Prints -225178692812801

classref-item-separator

classref-method

`int<class_int>` **to_argb32**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_to_argb32>`

Returns the color converted to a 32-bit integer in ARGB format (each component is 8 bits). ARGB is more compatible with DirectX.

gdscript

var color = Color(1, 0.5, 0.2) print(color.to_argb32()) \# Prints 4294934323

csharp

var color = new Color(1.0f, 0.5f, 0.2f); GD.Print(color.ToArgb32()); // Prints 4294934323

classref-item-separator

classref-method

`int<class_int>` **to_argb64**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_to_argb64>`

Returns the color converted to a 64-bit integer in ARGB format (each component is 16 bits). ARGB is more compatible with DirectX.

gdscript

var color = Color(1, 0.5, 0.2) print(color.to_argb64()) \# Prints -2147470541

csharp

var color = new Color(1.0f, 0.5f, 0.2f); GD.Print(color.ToArgb64()); // Prints -2147470541

classref-item-separator

classref-method

`String<class_String>` **to_html**(with_alpha: `bool<class_bool>` = true) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_to_html>`

Returns the color converted to an HTML hexadecimal color `String<class_String>` in RGBA format, without the hash (`#`) prefix.

Setting `with_alpha` to `false`, excludes alpha from the hexadecimal string, using RGB format instead of RGBA format.

gdscript

var white = Color(1, 1, 1, 0.5) var with_alpha = white.to_html() \# Returns "ffffff7f" var without_alpha = white.to_html(false) \# Returns "ffffff"

csharp

var white = new Color(1, 1, 1, 0.5f); string withAlpha = white.ToHtml(); // Returns "ffffff7f" string withoutAlpha = white.ToHtml(false); // Returns "ffffff"

classref-item-separator

classref-method

`int<class_int>` **to_rgba32**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_to_rgba32>`

Returns the color converted to a 32-bit integer in RGBA format (each component is 8 bits). RGBA is Godot's default format. This method is the inverse of `hex()<class_Color_method_hex>`.

gdscript

var color = Color(1, 0.5, 0.2) print(color.to_rgba32()) \# Prints 4286526463

csharp

var color = new Color(1, 0.5f, 0.2f); GD.Print(color.ToRgba32()); // Prints 4286526463

classref-item-separator

classref-method

`int<class_int>` **to_rgba64**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Color_method_to_rgba64>`

Returns the color converted to a 64-bit integer in RGBA format (each component is 16 bits). RGBA is Godot's default format. This method is the inverse of `hex64()<class_Color_method_hex64>`.

gdscript

var color = Color(1, 0.5, 0.2) print(color.to_rgba64()) \# Prints -140736629309441

csharp

var color = new Color(1, 0.5f, 0.2f); GD.Print(color.ToRgba64()); // Prints -140736629309441

classref-section-separator

classref-descriptions-group

## Operator Descriptions

classref-operator

`bool<class_bool>` **operator !=**(right: `Color<class_Color>`) `🔗<class_Color_operator_neq_Color>`

Returns `true` if the colors are not exactly equal.

**Note:** Due to floating-point precision errors, consider using `is_equal_approx()<class_Color_method_is_equal_approx>` instead, which is more reliable.

classref-item-separator

classref-operator

`Color<class_Color>` **operator**\*(right: `Color<class_Color>`) `🔗<class_Color_operator_mul_Color>`

Multiplies each component of the **Color** by the components of the given **Color**.

classref-item-separator

classref-operator

`Color<class_Color>` **operator**\*(right: `float<class_float>`) `🔗<class_Color_operator_mul_float>`

Multiplies each component of the **Color** by the given `float<class_float>`.

classref-item-separator

classref-operator

`Color<class_Color>` **operator**\*(right: `int<class_int>`) `🔗<class_Color_operator_mul_int>`

Multiplies each component of the **Color** by the given `int<class_int>`.

classref-item-separator

classref-operator

`Color<class_Color>` **operator +**(right: `Color<class_Color>`) `🔗<class_Color_operator_sum_Color>`

Adds each component of the **Color** with the components of the given **Color**.

classref-item-separator

classref-operator

`Color<class_Color>` **operator -**(right: `Color<class_Color>`) `🔗<class_Color_operator_dif_Color>`

Subtracts each component of the **Color** by the components of the given **Color**.

classref-item-separator

classref-operator

`Color<class_Color>` **operator /**(right: `Color<class_Color>`) `🔗<class_Color_operator_div_Color>`

Divides each component of the **Color** by the components of the given **Color**.

classref-item-separator

classref-operator

`Color<class_Color>` **operator /**(right: `float<class_float>`) `🔗<class_Color_operator_div_float>`

Divides each component of the **Color** by the given `float<class_float>`.

classref-item-separator

classref-operator

`Color<class_Color>` **operator /**(right: `int<class_int>`) `🔗<class_Color_operator_div_int>`

Divides each component of the **Color** by the given `int<class_int>`.

classref-item-separator

classref-operator

`bool<class_bool>` **operator ==**(right: `Color<class_Color>`) `🔗<class_Color_operator_eq_Color>`

Returns `true` if the colors are exactly equal.

**Note:** Due to floating-point precision errors, consider using `is_equal_approx()<class_Color_method_is_equal_approx>` instead, which is more reliable.

classref-item-separator

classref-operator

`float<class_float>` **operator \[\]**(index: `int<class_int>`) `🔗<class_Color_operator_idx_int>`

Access color components using their index. `[0]` is equivalent to `r<class_Color_property_r>`, `[1]` is equivalent to `g<class_Color_property_g>`, `[2]` is equivalent to `b<class_Color_property_b>`, and `[3]` is equivalent to `a<class_Color_property_a>`.

classref-item-separator

classref-operator

`Color<class_Color>` **operator unary+**() `🔗<class_Color_operator_unplus>`

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

classref-item-separator

classref-operator

`Color<class_Color>` **operator unary-**() `🔗<class_Color_operator_unminus>`

Inverts the given color. This is equivalent to `Color.WHITE - c` or `Color(1 - c.r, 1 - c.g, 1 - c.b, 1 - c.a)`. Unlike with `inverted()<class_Color_method_inverted>`, the `a<class_Color_property_a>` component is inverted, too.