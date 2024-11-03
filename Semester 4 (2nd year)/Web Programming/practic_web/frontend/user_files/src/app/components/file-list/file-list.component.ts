import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FileService } from '../../service/file.service';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-child-list',
    templateUrl: './file-list.component.html',
    styleUrls: ['./file-list.component.css'],
    standalone: true,
    imports: [CommonModule]
})
export class FileListComponent implements OnInit {
    files: any[] = [];
    allFiles: any[] = [];
    page = 1;
    maxPage = 1;
    id = "";
    filename = 'filename';

    constructor(private fileService: FileService, private router: Router) { }

    ngOnInit(): void {
        if (sessionStorage.getItem("user") == null) {
            this.router.navigate([' ']);
        }
        this.id = sessionStorage.getItem("user")!;
        console.log(this.id);
        this.page = 1;
        this.maxPage = 1;
        this.files = [];
        this.allFiles = [];
        this.filename = 'asdfasdfa';
        this.fileService.getFilesPaginated(1, sessionStorage.getItem("user")!).subscribe(files => {
            this.files = files;
            this.allFiles.push(...files);
            this.computeFilenameWithMostOccurences();
        });
    }

    nextPage(): void {
        this.page++;
        if (this.page > this.maxPage) {
            this.maxPage = this.page;
            this.fileService.getFilesPaginated(this.page, this.id).subscribe(files => {
                if (files.length == 0) {
                    alert("You are already on the last page");
                    this.page--;
                    return;
                }
                this.files = files;
                this.allFiles.push(...files);
                this.computeFilenameWithMostOccurences();
            });
        }
        else {
            this.fileService.getFilesPaginated(this.page, this.id).subscribe(files => {
                this.files = files;
            });
        }
    }

    previousPage(): void {
        if (this.page == 1) {
            alert("You are already on the first page");
            return;
        }
        this.page--;
        this.fileService.getFilesPaginated(this.page, this.id).subscribe(files => {
            this.files = files;
        });
    }

    computeFilenameWithMostOccurences(): void {
        let occurences: { [key: string]: number } = {};
        this.allFiles.forEach(file => {
            if (occurences[file.filename]) {
                occurences[file.filename]++;
            }
            else {
                occurences[file.filename] = 1;
            }
        });

        let maxOccurences = 0;
        let maxFilename = '';
        for (let filename in occurences) {
            if (occurences[filename] > maxOccurences) {
                maxOccurences = occurences[filename];
                maxFilename = filename;
            }
        }
        console.log(maxFilename);
        console.log(maxOccurences);
        console.log(occurences);
        this.filename = maxFilename;
    }


    logout(): void {
        sessionStorage.removeItem("user");
        this.router.navigate(['']);
    }
}