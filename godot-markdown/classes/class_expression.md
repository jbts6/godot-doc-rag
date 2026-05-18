github_url
hide

# Expression

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A class that stores an expression you can execute.

classref-introduction-group

## Description

An expression can be made of any arithmetic operation, built-in math function call, method call of a passed instance, or built-in type construction call.

An example expression text using the built-in math functions could be `sqrt(pow(3, 2) + pow(4, 2))`.

In the following example we use a `LineEdit<class_LineEdit>` node to write our expression and show the result.

gdscript

var expression = Expression.new()

func ready():
\$LineEdit.text_submitted.connect(self.\_on_text_submitted)

func on_text_submitted(command):
var error = expression.parse(command) if error != OK: print(expression.get_error_text()) return var result = expression.execute() if not expression.has_execute_failed(): \$LineEdit.text = str(result)

csharp

private Expression expression = new Expression();

public override void Ready() { GetNode\<LineEdit\>("LineEdit").TextSubmitted += OnTextEntered; }

private void OnTextEntered(string command) { Error error = expression.Parse(command); if (error != Error.Ok) { GD.Print(expression.GetErrorText()); return; } Variant result = expression.Execute(); if (!\_expression.HasExecuteFailed()) { GetNode\<LineEdit\>("LineEdit").Text = result.ToString(); } }

classref-introduction-group

## Tutorials

- `Evaluating Expressions <../tutorials/scripting/evaluating_expressions>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Variant<class_Variant>` **execute**(inputs: `Array<class_Array>` = \[\], base_instance: `Object<class_Object>` = null, show_error: `bool<class_bool>` = true, const_calls_only: `bool<class_bool>` = false) `🔗<class_Expression_method_execute>`

Executes the expression that was previously parsed by `parse()<class_Expression_method_parse>` and returns the result. Before you use the returned object, you should check if the method failed by calling `has_execute_failed()<class_Expression_method_has_execute_failed>`.

If you defined input variables in `parse()<class_Expression_method_parse>`, you can specify their values in the inputs array, in the same order.

classref-item-separator

classref-method

`String<class_String>` **get_error_text**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Expression_method_get_error_text>`

Returns the error text if `parse()<class_Expression_method_parse>` or `execute()<class_Expression_method_execute>` has failed.

classref-item-separator

classref-method

`bool<class_bool>` **has_execute_failed**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Expression_method_has_execute_failed>`

Returns `true` if `execute()<class_Expression_method_execute>` has failed.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **parse**(expression: `String<class_String>`, input_names: `PackedStringArray<class_PackedStringArray>` = PackedStringArray()) `🔗<class_Expression_method_parse>`

Parses the expression and returns an `Error<enum_@GlobalScope_Error>` code.

You can optionally specify names of variables that may appear in the expression with `input_names`, so that you can bind them when it gets executed.