import { TestBed } from '@angular/core/testing';

import { SScreeningService } from './s-screening.service';

describe('SScreeningService', () => {
  let service: SScreeningService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SScreeningService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
