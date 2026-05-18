github_url
hide

# XRFaceTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `XRTracker<class_XRTracker>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A tracked face.

classref-introduction-group

## Description

An instance of this object represents a tracked face and its corresponding blend shapes. The blend shapes come from the [Unified Expressions](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/unified-blendshapes) standard, and contain extended details and visuals for each blend shape. Additionally the [Tracking Standard Comparison](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/compatibility/overview) page documents the relationship between Unified Expressions and other standards.

As face trackers are turned on they are registered with the `XRServer<class_XRServer>`.

classref-introduction-group

## Tutorials

- `XR documentation index <../tutorials/xr/index>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **BlendShapeEntry**: `🔗<enum_XRFaceTracker_BlendShapeEntry>`

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_LOOK_OUT_RIGHT** = `0`

Right eye looks outwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_LOOK_IN_RIGHT** = `1`

Right eye looks inwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_LOOK_UP_RIGHT** = `2`

Right eye looks upwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_LOOK_DOWN_RIGHT** = `3`

Right eye looks downwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_LOOK_OUT_LEFT** = `4`

Left eye looks outwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_LOOK_IN_LEFT** = `5`

Left eye looks inwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_LOOK_UP_LEFT** = `6`

Left eye looks upwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_LOOK_DOWN_LEFT** = `7`

Left eye looks downwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_CLOSED_RIGHT** = `8`

Closes the right eyelid.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_CLOSED_LEFT** = `9`

Closes the left eyelid.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_SQUINT_RIGHT** = `10`

Squeezes the right eye socket muscles.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_SQUINT_LEFT** = `11`

Squeezes the left eye socket muscles.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_WIDE_RIGHT** = `12`

Right eyelid widens beyond relaxed.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_WIDE_LEFT** = `13`

Left eyelid widens beyond relaxed.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_DILATION_RIGHT** = `14`

Dilates the right eye pupil.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_DILATION_LEFT** = `15`

Dilates the left eye pupil.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_CONSTRICT_RIGHT** = `16`

Constricts the right eye pupil.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_CONSTRICT_LEFT** = `17`

Constricts the left eye pupil.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_PINCH_RIGHT** = `18`

Right eyebrow pinches in.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_PINCH_LEFT** = `19`

Left eyebrow pinches in.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_LOWERER_RIGHT** = `20`

Outer right eyebrow pulls down.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_LOWERER_LEFT** = `21`

Outer left eyebrow pulls down.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_INNER_UP_RIGHT** = `22`

Inner right eyebrow pulls up.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_INNER_UP_LEFT** = `23`

Inner left eyebrow pulls up.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_OUTER_UP_RIGHT** = `24`

Outer right eyebrow pulls up.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_OUTER_UP_LEFT** = `25`

Outer left eyebrow pulls up.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NOSE_SNEER_RIGHT** = `26`

Right side face sneers.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NOSE_SNEER_LEFT** = `27`

Left side face sneers.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NASAL_DILATION_RIGHT** = `28`

Right side nose canal dilates.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NASAL_DILATION_LEFT** = `29`

Left side nose canal dilates.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NASAL_CONSTRICT_RIGHT** = `30`

Right side nose canal constricts.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NASAL_CONSTRICT_LEFT** = `31`

Left side nose canal constricts.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_CHEEK_SQUINT_RIGHT** = `32`

Raises the right side cheek.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_CHEEK_SQUINT_LEFT** = `33`

Raises the left side cheek.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_CHEEK_PUFF_RIGHT** = `34`

Puffs the right side cheek.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_CHEEK_PUFF_LEFT** = `35`

Puffs the left side cheek.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_CHEEK_SUCK_RIGHT** = `36`

Sucks in the right side cheek.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_CHEEK_SUCK_LEFT** = `37`

Sucks in the left side cheek.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_JAW_OPEN** = `38`

Opens jawbone.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_CLOSED** = `39`

Closes the mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_JAW_RIGHT** = `40`

Pushes jawbone right.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_JAW_LEFT** = `41`

Pushes jawbone left.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_JAW_FORWARD** = `42`

Pushes jawbone forward.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_JAW_BACKWARD** = `43`

Pushes jawbone backward.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_JAW_CLENCH** = `44`

Flexes jaw muscles.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_JAW_MANDIBLE_RAISE** = `45`

Raises the jawbone.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_SUCK_UPPER_RIGHT** = `46`

Upper right lip part tucks in the mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_SUCK_UPPER_LEFT** = `47`

Upper left lip part tucks in the mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_SUCK_LOWER_RIGHT** = `48`

Lower right lip part tucks in the mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_SUCK_LOWER_LEFT** = `49`

Lower left lip part tucks in the mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_SUCK_CORNER_RIGHT** = `50`

Right lip corner folds into the mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_SUCK_CORNER_LEFT** = `51`

Left lip corner folds into the mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_FUNNEL_UPPER_RIGHT** = `52`

Upper right lip part pushes into a funnel.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_FUNNEL_UPPER_LEFT** = `53`

Upper left lip part pushes into a funnel.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_FUNNEL_LOWER_RIGHT** = `54`

Lower right lip part pushes into a funnel.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_FUNNEL_LOWER_LEFT** = `55`

Lower left lip part pushes into a funnel.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_PUCKER_UPPER_RIGHT** = `56`

Upper right lip part pushes outwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_PUCKER_UPPER_LEFT** = `57`

Upper left lip part pushes outwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_PUCKER_LOWER_RIGHT** = `58`

Lower right lip part pushes outwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_PUCKER_LOWER_LEFT** = `59`

Lower left lip part pushes outwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_UPPER_UP_RIGHT** = `60`

Upper right part of the lip pulls up.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_UPPER_UP_LEFT** = `61`

Upper left part of the lip pulls up.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_LOWER_DOWN_RIGHT** = `62`

Lower right part of the lip pulls up.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_LOWER_DOWN_LEFT** = `63`

Lower left part of the lip pulls up.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_UPPER_DEEPEN_RIGHT** = `64`

Upper right lip part pushes in the cheek.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_UPPER_DEEPEN_LEFT** = `65`

Upper left lip part pushes in the cheek.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_UPPER_RIGHT** = `66`

Moves upper lip right.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_UPPER_LEFT** = `67`

Moves upper lip left.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_LOWER_RIGHT** = `68`

Moves lower lip right.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_LOWER_LEFT** = `69`

Moves lower lip left.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_CORNER_PULL_RIGHT** = `70`

Right lip corner pulls diagonally up and out.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_CORNER_PULL_LEFT** = `71`

Left lip corner pulls diagonally up and out.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_CORNER_SLANT_RIGHT** = `72`

Right corner lip slants up.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_CORNER_SLANT_LEFT** = `73`

Left corner lip slants up.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_FROWN_RIGHT** = `74`

Right corner lip pulls down.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_FROWN_LEFT** = `75`

Left corner lip pulls down.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_STRETCH_RIGHT** = `76`

Mouth corner lip pulls out and down.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_STRETCH_LEFT** = `77`

Mouth corner lip pulls out and down.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_DIMPLE_RIGHT** = `78`

Right lip corner is pushed backwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_DIMPLE_LEFT** = `79`

Left lip corner is pushed backwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_RAISER_UPPER** = `80`

Raises and slightly pushes out the upper mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_RAISER_LOWER** = `81`

Raises and slightly pushes out the lower mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_PRESS_RIGHT** = `82`

Right side lips press and flatten together vertically.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_PRESS_LEFT** = `83`

Left side lips press and flatten together vertically.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_TIGHTENER_RIGHT** = `84`

Right side lips squeeze together horizontally.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_TIGHTENER_LEFT** = `85`

Left side lips squeeze together horizontally.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_OUT** = `86`

Tongue visibly sticks out of the mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_UP** = `87`

Tongue points upwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_DOWN** = `88`

Tongue points downwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_RIGHT** = `89`

Tongue points right.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_LEFT** = `90`

Tongue points left.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_ROLL** = `91`

Sides of the tongue funnel, creating a roll.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_BLEND_DOWN** = `92`

Tongue arches up then down inside the mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_CURL_UP** = `93`

Tongue arches down then up inside the mouth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_SQUISH** = `94`

Tongue squishes together and thickens.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_FLAT** = `95`

Tongue flattens and thins out.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_TWIST_RIGHT** = `96`

Tongue tip rotates clockwise, with the rest following gradually.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_TONGUE_TWIST_LEFT** = `97`

Tongue tip rotates counter-clockwise, with the rest following gradually.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_SOFT_PALATE_CLOSE** = `98`

Inner mouth throat closes.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_THROAT_SWALLOW** = `99`

The Adam's apple visibly swallows.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NECK_FLEX_RIGHT** = `100`

Right side neck visibly flexes.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NECK_FLEX_LEFT** = `101`

Left side neck visibly flexes.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_CLOSED** = `102`

Closes both eye lids.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_WIDE** = `103`

Widens both eye lids.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_SQUINT** = `104`

Squints both eye lids.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_DILATION** = `105`

Dilates both pupils.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_EYE_CONSTRICT** = `106`

Constricts both pupils.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_DOWN_RIGHT** = `107`

Pulls the right eyebrow down and in.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_DOWN_LEFT** = `108`

Pulls the left eyebrow down and in.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_DOWN** = `109`

Pulls both eyebrows down and in.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_UP_RIGHT** = `110`

Right brow appears worried.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_UP_LEFT** = `111`

Left brow appears worried.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_BROW_UP** = `112`

Both brows appear worried.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NOSE_SNEER** = `113`

Entire face sneers.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NASAL_DILATION** = `114`

Both nose canals dilate.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_NASAL_CONSTRICT** = `115`

Both nose canals constrict.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_CHEEK_PUFF** = `116`

Puffs both cheeks.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_CHEEK_SUCK** = `117`

Sucks in both cheeks.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_CHEEK_SQUINT** = `118`

Raises both cheeks.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_SUCK_UPPER** = `119`

Tucks in the upper lips.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_SUCK_LOWER** = `120`

Tucks in the lower lips.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_SUCK** = `121`

Tucks in both lips.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_FUNNEL_UPPER** = `122`

Funnels in the upper lips.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_FUNNEL_LOWER** = `123`

Funnels in the lower lips.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_FUNNEL** = `124`

Funnels in both lips.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_PUCKER_UPPER** = `125`

Upper lip part pushes outwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_PUCKER_LOWER** = `126`

Lower lip part pushes outwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_LIP_PUCKER** = `127`

Lips push outwards.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_UPPER_UP** = `128`

Raises the upper lips.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_LOWER_DOWN** = `129`

Lowers the lower lips.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_OPEN** = `130`

Mouth opens, revealing teeth.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_RIGHT** = `131`

Moves mouth right.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_LEFT** = `132`

Moves mouth left.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_SMILE_RIGHT** = `133`

Right side of the mouth smiles.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_SMILE_LEFT** = `134`

Left side of the mouth smiles.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_SMILE** = `135`

Mouth expresses a smile.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_SAD_RIGHT** = `136`

Right side of the mouth expresses sadness.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_SAD_LEFT** = `137`

Left side of the mouth expresses sadness.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_SAD** = `138`

Mouth expresses sadness.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_STRETCH** = `139`

Mouth stretches.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_DIMPLE** = `140`

Lip corners dimple.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_TIGHTENER** = `141`

Mouth tightens.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MOUTH_PRESS** = `142`

Mouth presses together.

classref-enumeration-constant

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` **FT_MAX** = `143`

Represents the size of the `BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`PackedFloat32Array<class_PackedFloat32Array>` **blend_shapes** = `PackedFloat32Array()` `🔗<class_XRFaceTracker_property_blend_shapes>`

classref-property-setget

- `void (No return value.)` **set_blend_shapes**(value: `PackedFloat32Array<class_PackedFloat32Array>`)
- `PackedFloat32Array<class_PackedFloat32Array>` **get_blend_shapes**()

The array of face blend shape weights with indices corresponding to the `BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>` enum.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedFloat32Array<class_PackedFloat32Array>` for more details.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_blend_shape**(blend_shape: `BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRFaceTracker_method_get_blend_shape>`

Returns the requested face blend shape weight.

classref-item-separator

classref-method

`void (No return value.)` **set_blend_shape**(blend_shape: `BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`, weight: `float<class_float>`) `🔗<class_XRFaceTracker_method_set_blend_shape>`

Sets a face blend shape weight.