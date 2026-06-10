# Detailed Line-by-Line Explanation of the Caesar Cipher Program

## Import Statement
```java
import java.util.Scanner;
```
**Purpose**: Imports the Scanner class from Java's utility library, which allows the program to read user input from the keyboard.

## Class Declaration
```java
public class CaesarCipher {
```
**Purpose**: Declares a public class named `CaesarCipher`. The `public` keyword means this class can be accessed from anywhere. All Java code must be inside a class.

## ALPHABET String Declaration
```java
private static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
```
**Purpose**: Creates a constant string containing all 26 uppercase letters.
- `private`: Only accessible within this class
- `static`: Belongs to the class itself, not to any specific instance
- `final`: Cannot be changed after initialization (constant)
- The index position (0-25) represents each letter's numeric value (A=0, B=1, ..., Z=25)

## Main Method Declaration
```java
public static void main(String[] args) {
```
**Purpose**: The program's entry point. Java always looks for this exact method signature to start execution.

## Scanner Object Creation
```java
Scanner scanner = new Scanner(System.in);
```
**Purpose**: Creates a Scanner object that reads from `System.in` (standard input/keyboard). This object will be used to get user input.

## Reading Plaintext Input
```java
System.out.print("Enter the plaintext to encrypt: ");
```
**Purpose**: Displays a prompt message to the user without moving to a new line (print vs println).

```java
String plaintext = scanner.nextLine().toUpperCase();
```
**Purpose**: 
- `scanner.nextLine()`: Reads the entire line of text the user types
- `.toUpperCase()`: Converts all characters to uppercase
- `String plaintext`: Stores the converted input in a String variable

## Reading the Cipher Key
```java
System.out.print("Enter the Caesar cipher key (integer between 0 and 25): ");
```
**Purpose**: Prompts user for the encryption/decryption key.

```java
int key = scanner.nextInt();
```
**Purpose**: Reads an integer value from the user and stores it in the `key` variable.

## Input Validation
```java
if (key < 0 || key > 25) {
```
**Purpose**: Checks if the key is outside the valid range (0-25). The `||` operator means "OR".

```java
System.out.println("Error: Key must be between 0 and 25. Using key = 0.");
```
**Purpose**: Displays an error message if the key is invalid.

```java
key = 0;
```
**Purpose**: Resets the invalid key to a default safe value (0 means no shift).

## Encryption Step
```java
String ciphertext = encrypt(plaintext, key);
```
**Purpose**: Calls the `encrypt` method, passing the plaintext and key as arguments, and stores the returned encrypted text in `ciphertext`.

```java
System.out.println("\nEncrypted ciphertext: " + ciphertext);
```
**Purpose**: Displays the encrypted text. The `\n` adds a blank line before the output for better formatting.

## Decryption Step
```java
String decryptedText = decrypt(ciphertext, key);
```
**Purpose**: Calls the `decrypt` method, passing the ciphertext and the same key, and stores the decrypted result.

```java
System.out.println("Decrypted plaintext: " + decryptedText);
```
**Purpose**: Displays the decrypted text to verify it matches the original input.

```java
scanner.close();
```
**Purpose**: Closes the Scanner object to prevent resource leaks (good practice).

## Encrypt Method - Method Signature
```java
public static String encrypt(String plaintext, int key) {
```
**Purpose**: Method header declaring:
- `public`: Can be called from anywhere
- `static`: Can be called without creating an object
- `String`: Return type (returns encrypted text)
- `encrypt`: Method name
- `String plaintext, int key`: Parameters the method receives

## StringBuilder Creation
```java
StringBuilder ciphertext = new StringBuilder();
```
**Purpose**: Creates a mutable string object for efficient string building. Unlike regular Strings, StringBuilder can be modified without creating new objects each time.

## For Loop - Character Processing
```java
for (int i = 0; i < plaintext.length(); i++) {
```
**Purpose**: Loops through each character in the plaintext string:
- `int i = 0`: Starts at index 0
- `i < plaintext.length()`: Continues until reaching the string's length
- `i++`: Increments index by 1 each iteration

## Getting Current Character
```java
char currentChar = plaintext.charAt(i);
```
**Purpose**: Retrieves the character at position `i` from the plaintext string.

## Finding Character's Numeric Value
```java
int plainNumeric = ALPHABET.indexOf(currentChar);
```
**Purpose**: Searches for `currentChar` in the ALPHABET string and returns its index position (0-25). Returns -1 if the character isn't found (e.g., space, punctuation).

## Checking if Character is a Letter
```java
if (plainNumeric != -1) {
```
**Purpose**: If the character was found in ALPHABET (not -1), it's a letter that can be encrypted. Otherwise, it's a non-alphabetic character.

## Encryption Calculation
```java
int cipherNumeric = (plainNumeric + key) % 26;
```
**Purpose**: Applies the Caesar cipher formula:
- Adds the key to the plaintext numeric value
- `% 26` (modulo) wraps around the alphabet (e.g., Z (25) + 1 = 26 % 26 = 0, which is A)

## Getting Cipher Character
```java
char cipherChar = ALPHABET.charAt(cipherNumeric);
```
**Purpose**: Retrieves the character at position `cipherNumeric` from ALPHABET, converting the numeric value back to a letter.

## Appending to Result
```java
ciphertext.append(cipherChar);
```
**Purpose**: Adds the encrypted character to the StringBuilder.

## Handling Non-Alphabetic Characters
```java
} else {
    ciphertext.append(currentChar);
}
```
**Purpose**: If the character wasn't a letter (space, number, punctuation), keep it unchanged and append as-is.

## Returning Encrypted Text
```java
return ciphertext.toString();
```
**Purpose**: Converts the StringBuilder to a regular String and returns it to the caller.

## Decrypt Method - Similar Structure
```java
public static String decrypt(String ciphertext, int key) {
```
**Purpose**: Method header for decryption.

## Decryption Loop
```java
for (int i = 0; i < ciphertext.length(); i++) {
    char currentChar = ciphertext.charAt(i);
    int cipherNumeric = ALPHABET.indexOf(currentChar);
```
**Purpose**: Same as encryption - iterates through each character and finds its numeric value.

## Decryption Calculation
```java
int plainNumeric = (cipherNumeric - key) % 26;
```
**Purpose**: Reverses the encryption by subtracting the key.

## Handling Negative Values
```java
if (plainNumeric < 0) {
    plainNumeric = plainNumeric + 26;
}
```
**Purpose**: In Java, `%` can return negative numbers. This adjusts negative values by adding 26 to get the correct positive index (e.g., -1 + 26 = 25, which is Z).

## Getting Plaintext Character
```java
char plainChar = ALPHABET.charAt(plainNumeric);
plaintext.append(plainChar);
```
**Purpose**: Converts the numeric value back to a letter and appends it to the result.

## Final Return
```java
return plaintext.toString();
```
**Purpose**: Returns the decrypted string to the main method.

## Example Execution Flow:
1. User inputs: "HELLO" with key=3
2. H (index 7) → (7+3)%26 = 10 → K
3. E (index 4) → (4+3)%26 = 7 → H
4. L (index 11) → (11+3)%26 = 14 → O
5. L (index 11) → (11+3)%26 = 14 → O
6. O (index 14) → (14+3)%26 = 17 → R
7. Result: "KHOOR"
