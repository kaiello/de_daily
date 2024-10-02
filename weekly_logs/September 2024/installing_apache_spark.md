# Installing and Verifying Apache Spark 3.5.3

## Step 1: Install Java 8
Java 8 is the most widely compatible and stable version for Spark.

Download it from [here](https://www.java.com/download/ie_manual.jsp).

## Step 2: Download Spark
You can download Spark from the following link:

[Download Spark 3.5.3 (Pre-built for Hadoop 3)](https://www.apache.org/dyn/closer.lua/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz)

## Step 3: Extract the TAR File
After downloading the TAR file, move it to your desired location and extract it. 

### On Windows:
1. Open a terminal (Git Bash or Command Prompt).
2. Navigate to the folder where the file is located.
3. Use the following command to extract the TAR file:

    ```bash
    tar -xvzf spark-3.5.3-bin-hadoop3.tgz
    ```

After extraction, you will have a folder named `spark-3.5.3-bin-hadoop3`.

## Step 4: Download and Verify the PGP Signature

To ensure the integrity of the Spark download, verify its checksum and signature.

### Step 4.1: Download the SHA-512 Checksum and PGP Signature
- Download the [KEYS file](https://downloads.apache.org/spark/KEYS) - I downloaded this as a text file from the browser.
- Download the [PGP signature file](https://downloads.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz.asc).

### Step 4.2: Verify the SHA-512 Checksum
Use the following command in **Command Prompt** (run as Administrator) to verify the SHA-512 checksum:

```bash
certutil -hashfile C:\path\to\your\spark-3.5.3-bin-hadoop3.tgz SHA512
```

### Step 4.3: Import the KEYS File in Git Bash
In **Git Bash**, navigate to the directory where the `KEYS` file is located and import it:

```bash
cat KEYS.txt # to confirm the key
gpg --import KEYS.txt
```

### Step 4.4: Verify the PGP Signature
Verify the PGP signature with the following command:

```bash
gpg --verify spark-3.5.3-bin-hadoop3.tgz.asc spark-3.5.3-bin-hadoop3.tgz
```

### Step 4.5: (Optional) Download the `.asc` File Using Curl
If necessary, you can use `curl` to download the `.asc` file:

```bash
curl -O -k https://downloads.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz.asc
```

### Step 4.6: Checking GPG Fingerprint
To ensure that the PGP key is trusted, check its fingerprint:

```bash
gpg --fingerprint 0A2D660358B6F6F8071FD16F6606986CF5A8447C
```

## Step 4.7:
By following these steps, you’ve successfully installed Apache Spark and verified are able to check the authenticity using both SHA-512 checksums and PGP signatures.

For more information on verifying Apache software releases, visit the [official Apache verification guide](https://www.apache.org/info/verification.html).

Most Apache HTTP Server developers have signed each other's keys, typically through face-to-face verification. As a result, to join the web of trust, you generally only need to verify one person within that network. (Tip: all the developers' keys are included in the KEYS file.) After running the `gpg --import KEYS.txt` command, you can search for the Apache developers using the `@apache.org` domain in their email addresses.

# Step 5: Adding Spark to the System's PATH Variable on Windows

## Step 5.1: Open System Properties
- Press **Win + X** and select **System**.
- In the window that opens, click **Advanced system settings** on the left.
- In the **System Properties** window, click the **Environment Variables** button near the bottom.

## Step 5.2: Add `SPARK_HOME` Environment Variable
- In the **Environment Variables** window, under **System variables**, click **New**.
- In the **Variable name** field, enter `SPARK_HOME`.
- In the **Variable value** field, enter the path to your Spark installation directory (for example, `C:\\spark\\spark-3.5.3-bin-hadoop3`).
- Click **OK** to save.

## Step 5.3: Add Spark to the PATH Variable
- In the **Environment Variables** window, under **System variables**, scroll to find the **Path** variable and select it. Then click **Edit**.
- In the **Edit Environment Variable** dialog, click **New**.
- Add the path to Spark's `bin` folder, which is inside the directory you installed Spark into. For example:

    ```plaintext
    C:\\spark\\spark-3.5.3-bin-hadoop3\\bin
    ```

- Click **OK** to save.

## Step 5.4: Restart Command Prompt or Git Bash
- After modifying the environment variables, restart any open terminal windows (Command Prompt, Git Bash, etc.) for the changes to take effect.

## Step 5.5: Verify the Installation
 Once you've updated your PATH, you can verify that Spark has been successfully added by opening a new Command Prompt or Git Bash window and running:

    ```bash
    spark-shell
    ```

- If the Spark shell starts without errors, Spark is now correctly added to your PATH and ready to use.

